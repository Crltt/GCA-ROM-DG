import numpy as np
import torch
from torch_geometric.data import Data
from torch_geometric.loader import DataLoader
from gca_rom_dg import scaling


def graphs_dataset(dataset, HyperParams):
    """
    graphs_dataset: function to process and scale the input dataset for graph autoencoder model.

    Inputs:
    dataset: an object containing the dataset to be processed.
    HyperParams: an object containing the hyperparameters of the graph autoencoder model.

    Outputs:
    dataset_graph: an object containing the processed and scaled dataset.
    loader: a DataLoader object of the processed and scaled dataset.
    train_loader: a DataLoader object of the training set.
    test_loader: a DataLoader object of the test set.
    val_loader: a DataLoader object of the validation set.
    scaler_all: a scaler object to scale the entire dataset.
    scaler_test: a scaler object to scale the test set.
    xyz: an list containig array of the x, y and z-coordinate of the nodes.
    var: an array of the node features.
    VAR_all: an array of the scaled node features of the entire dataset.
    VAR_test: an array of the scaled node features of the test set.
    train_snapshots: a list of indices of the training set.
    test_snapshots: a list of indices of the test set.
    """

    #coordx = dataset.coordx
    #coordy = dataset.coordy
    #coordxyz = [coordx, coordy]
    
    xx = dataset.xx
    yy = dataset.yy
    xyz = [xx, yy]
    dof = int(dataset.dof)
    if dataset.dim == 3:
       coordz = dataset.coordz
       #coordxyz.append(coordz)
        
       zz = dataset.zz
       xyz.append(zz)
    var = dataset.U

    # PROCESSING DATASET
    #num_nodes = int(var.shape[0]/3)
    num_nodes = int(var.shape[0]/dof)
    num_graphs = int(var.shape[1]) 

    print('num_nodes: ', num_nodes)
    print('num_graphs: ', num_graphs)

    total_sims = int(num_graphs)
    rate = HyperParams.rate/100
    train_sims = int(rate * total_sims)
    test_sims = total_sims - train_sims
    main_loop = np.arange(total_sims).tolist()
    np.random.shuffle(main_loop)

    train_snapshots = main_loop[0:train_sims]
    train_snapshots.sort()
    test_snapshots = main_loop[train_sims:total_sims]
    test_snapshots.sort()

    ## FEATURE SCALING
    var_test = dataset.U[:, test_snapshots]  

    scaling_type = HyperParams.scaling_type
    scaler_all, VAR_all = scaling.tensor_scaling(var, scaling_type, HyperParams.scaler_number)
    scaler_test, VAR_test = scaling.tensor_scaling(var_test, scaling_type, HyperParams.scaler_number)

    graphs = []
    edge_index = torch.t(dataset.E)-1
    for graph in range(num_graphs):
        if dataset.dim == 2:
            # pos = torch.cat((xx[:, graph].unsqueeze(1), yy[:, graph].unsqueeze(1)), 1) 
            pos = torch.cat((xx[:, 1].unsqueeze(1), yy[:, 1].unsqueeze(1)), 1)
        elif dataset.dim == 3:
            pos = torch.cat((xx[:, graph].unsqueeze(1), yy[:, graph].unsqueeze(1), zz[:, graph].unsqueeze(1)), 1)
        ei = torch.index_select(pos, 0, edge_index[0, :])
        ej = torch.index_select(pos, 0, edge_index[1, :])
        edge_diff = ej - ei
        if dataset.dim == 2:
            edge_attr = torch.sqrt(torch.pow(edge_diff[:, 0], 2) + torch.pow(edge_diff[:, 1], 2))
        elif dataset.dim == 3:
            edge_attr = torch.sqrt(torch.pow(edge_diff[:, 0], 2) + torch.pow(edge_diff[:, 1], 2) + torch.pow(edge_diff[:, 2], 2))
        node_features_list = VAR_all[graph, :]  
        N = node_features_list.shape[0]
        #M = int(3) 
        M = dof
        #node_features = node_features_list.reshape(int(N/3),3)
        node_features = node_features_list.reshape(int(N/int(dof)),int(dof))
        dataset_graph = Data(x=node_features, edge_index=edge_index, edge_attr=edge_attr, pos=pos)
        graphs.append(dataset_graph)

    #HyperParams.dof = dof
    
    HyperParams.num_nodes = dataset_graph.num_nodes
    train_dataset = [graphs[i] for i in train_snapshots]
    test_dataset = [graphs[i] for i in test_snapshots]

    print("Length of train dataset: ", len(train_dataset))
    print("Length of test dataset: ", len(test_dataset))

    loader = DataLoader(graphs, batch_size=1)
    train_loader = DataLoader(train_dataset, batch_size=train_sims, shuffle=False)
    test_loader = DataLoader(test_dataset, batch_size=test_sims, shuffle=False)
    val_loader = DataLoader(test_dataset, batch_size=1, shuffle=False)
    
    return loader, train_loader, test_loader, \
            val_loader, scaler_all, scaler_test, xyz, VAR_all, VAR_test, \
                train_snapshots, test_snapshots

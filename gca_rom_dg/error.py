import numpy as np
import torch
from gca_rom_dg import scaling


def save_error(error, norm, HyperParams, vars):
    """
    save_error(error: List[float], norm: List[float], HyperParams: object, vars: str)

    This function takes in two lists of same length, error and norm, computed on the whole dataset for plotting reasons, and saves the relative error, along with the max, mean and min to a txt file.

    The relative error is calculated as error/norm for each corresponding element. The file is saved with a specific naming convention: HyperParams.net_dir + 'relative_errors' + HyperParams.net_run + vars + '.txt'

    Parameters:
    error (List[float]): A list of error values.
    norm (List[float]): A list of norm values of same length as error.
    HyperParams (object): An object containing information required to form the file name.
    vars (str): A string to be appended to the file name.
    """

    error = np.array(error)
    norm = np.array(norm)
    rel_error = error/norm
    np.savetxt(HyperParams.net_dir+'relative_errors'+HyperParams.net_run+vars+'.txt', [max(rel_error), sum(rel_error)/len(rel_error), min(rel_error)])


def print_error(error, norm, vars):
    """
    print_error(error: List[float], norm: List[float], vars: str)

    This function takes in two lists error and norm of same length and prints their absolute and relative errors, along with the max, mean and min of both the absolute and relative errors.

    The relative error is calculated as error/norm for each corresponding elements.

    Parameters:
    error (List[float]): A list of error values.
    norm (List[float]): A list of norm values of same length as error.
    vars (str): A string to describe the type of field.
    """

    error = np.array(error)
    norm = np.array(norm)
    rel_error = error/norm
    print("\nMaximum absolute error for field "+vars+" = ", max(error))
    print("Mean absolute error for field "+vars+" = ", sum(error)/len(error))
    print("Minimum absolute error for field "+vars+" = ", min(error))
    print("\nMaximum relative error for field "+vars+" = ", max(rel_error))
    print("Mean relative error for field "+vars+" = ", sum(rel_error)/len(rel_error))
    print("Minimum relative error for field "+vars+" = ", min(rel_error))


def compute_error(res, VAR, scaler, HyperParams):
    """
    Compute the absolute error and norm between the original data and the data generated by the autoencoder

    :param res: Resulting data generated by the autoencoder (numpy ndarray)
    :param VAR: Original data (numpy ndarray)
    :param scaler: Scaler object for scaling the data
    :param HyperParams: Autoencoder parameters (object)
    :return: error_abs_list, norm_z_list, lists of absolute error and norm for each snapshot of data
    """

    error_abs_list = list()
    norm_z_list = list()
    Z = scaling.inverse_scaling(VAR, scaler, HyperParams.scaling_type)
    Z_net = scaling.inverse_scaling(res.reshape(VAR.shape[0],VAR.shape[1],1), scaler, HyperParams.scaling_type)
    for snap in range(VAR.shape[0]):
        #error_abs = np.linalg.norm(abs(Z[:, snap] - Z_net[:, snap]))
        #norm_z = np.linalg.norm(Z[:, snap], 2)
        error_abs = np.linalg.norm(abs(VAR[snap,:,:] - res.reshape(VAR.shape[0],VAR.shape[1],1)[snap,:,:]))
        norm_z = np.linalg.norm(VAR[snap,:,:], 2)
        error_abs_list.append(error_abs)
        norm_z_list.append(norm_z)
    return error_abs_list, norm_z_list

def compute_analytic_error(res,dataset,test_snapshots, scaler, HyperParams):
    """
    Compute the absolute error and norm between the snalytic solution data and the data generated by the autoencoder

    :param res: Resulting data generated by the autoencoder (numpy ndarray)
    :param VAR: Original data (numpy ndarray)
    :param scaler: Scaler object for scaling the data
    :param HyperParams: Autoencoder parameters (object)
    :return: error_abs_list, norm_z_list, lists of absolute error and norm for each snapshot of data
    """

    xx = dataset.xx
    yy = dataset.yy
    x = xx[:,1]
    y = yy[:,1]
  
    error_abs_list = list()
    norm_z_list = list()

    a_sol_matr = np.empty((res.shape[0],int(x.shape[0])))
    for snap in range(res.shape[0]):
      a_sol = np.sin(np.pi*x)*np.sin(np.pi*y)*np.cos(np.sqrt(2)*(int(test_snapshots[snap]))*0.0005747126)
      a_sol_matr[snap,:] = a_sol
   

    a_sol_tensor = torch.tensor(a_sol_matr).reshape(res.shape[0],x.shape[0],6)
    print(a_sol_tensor.shape)
    print(res.shape)
    print('a_sol',a_sol_tensor.shape)
    Z = scaling.inverse_scaling(a_sol_tensor, scaler, HyperParams.scaling_type)
    Z_net = scaling.inverse_scaling(res, scaler, HyperParams.scaling_type)
    print('Z',Z.shape)
    print('Z_net',Z_net.shape)
    for snap in range(res.shape[0]):
        error_abs = np.linalg.norm(abs(Z[:, snap] - Z_net[:, snap]))
        norm_z = np.linalg.norm(Z[:, snap], 2)
        error_abs_list.append(error_abs)
        norm_z_list.append(norm_z)
    return error_abs_list, norm_z_list, a_sol_tensor

import numpy as np


def problem(argument):
    """
    problem(argument: int) -> Tuple[str, str, np.ndarray, np.ndarray]

    This function takes in an integer argument and returns a tuple containing the problem name (str), variable name (str), mu1 (np.ndarray) and mu2 (np.ndarray) for the specified case.

    The possible values of argument are:


    Returns:
    Tuple containing the problem name (str), variable name (str), mu1 (np.ndarray) and mu2 (np.ndarray) for the specified case.
    """

    match argument:
        case 24:
            problem_name = "maxwelldg00625p1hp"
            variable = 'TEz'
            mu1 = np.linspace(0.0035,int(1/6),245)
            mu_space = [mu1]
            n_param = 1
        case 25:
            problem_name = "maxwelldg00625p1hp"
            variable = 'THx'
            mu1 = np.linspace(1, 300,300)
            mu2 = np.linspace(1,1,300)
            mu_space = [mu1, mu2]
            n_param = 2
        case 26:
            problem_name = "maxwelldg00625p1hp"
            variable = 'THy'
            mu1 = np.linspace(1, 300,300)
            mu2 = np.linspace(1,1,300)
            mu_space = [mu1, mu2]
            n_param = 2
        case 27:
            problem_name = "maxwelldg00625p2hp"
            variable = 'TEz'
            mu1 = np.linspace(1, 290,290)
            mu2 = np.linspace(1,1,290)
            mu_space = [mu1, mu2]
            n_param = 2
        case 28:
            problem_name = "maxwelldg00625p2hp"
            variable = 'THx'
            mu1 = np.linspace(1, 290,290)
            mu2 = np.linspace(1,1,290)
            mu_space = [mu1, mu2]
            n_param = 2
        case 29:
            problem_name = "maxwelldg00625p2hp"
            variable = 'THy'
            mu1 = np.linspace(1, 290,290)
            mu2 = np.linspace(1,1,290)
            mu_space = [mu1, mu2]
            n_param = 2 
        case 30:
            problem_name = "maxwelldgparam"
            variable = 'TEz'
            mu1 = np.linspace(1, 300,300)
            mu2 = [np.linspace(1,1,30)*8.451365660882516, np.linspace(1,1,30)*8.150576639168921, np.linspace(1,1,30)*9.657458497408417,np.linspace(1,1,30)*9.325449970024170, np.linspace(1,1,30)*9.07716175885174, np.linspace(1,1,30)*7.163933478590142, np.linspace(1,1,30)*6.880812768081277, np.linspace(1,1,30)*8.590706586245833, np.linspace(1,1,30)*8.459595371133265, np.linspace(1,1,30)*8.328310981355269]
            mu_space = [mu1, mu2]
            n_param = 2
        case 31:
            problem_name = "maxwelldgparam"
            variable = 'THx'
            mu1 = np.linspace(1, 300,300)
            mu2 = [np.linspace(1,1,30)*8.451365660882516, np.linspace(1,1,30)*8.150576639168921, np.linspace(1,1,30)*9.657458497408417,np.linspace(1,1,30)*9.325449970024170, np.linspace(1,1,30)*9.07716175885174, np.linspace(1,1,30)*7.163933478590142, np.linspace(1,1,30)*6.880812768081277, np.linspace(1,1,30)*8.590706586245833, np.linspace(1,1,30)*8.459595371133265, np.linspace(1,1,30)*8.328310981355269]
            mu_space = [mu1, mu2]
            n_param = 2
        case 32:
            problem_name = "maxwelldgparam"
            variable = 'THy'
            mu1 = np.linspace(1, 300,300)
            mu2 = [np.linspace(1,1,30)*8.451365660882516, np.linspace(1,1,30)*8.150576639168921, np.linspace(1,1,30)*9.657458497408417,np.linspace(1,1,30)*9.325449970024170, np.linspace(1,1,30)*9.07716175885174, np.linspace(1,1,30)*7.163933478590142, np.linspace(1,1,30)*6.880812768081277, np.linspace(1,1,30)*8.590706586245833, np.linspace(1,1,30)*8.459595371133265, np.linspace(1,1,30)*8.328310981355269]
            n_param = 2 
    return problem_name, variable, mu_space, n_param

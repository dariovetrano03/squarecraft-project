class AeronauticConstants:
    # Sea level standard conditions
    RHO_0 = 1.225        # kg/m^3
    T_0 = 288.15         # K
    P_0 = 101_325        # Pa
    A_0 = 340.294        # m/s

    # Physical constants
    G_0 = 9.80665        # m/s^2
    R = 287.053          # J/(kg·K)
    GAMMA = 1.4
    CP = 1004.5
    CV = CP / GAMMA

    # Temperature lapse rates
    L_TROP = -0.0065
    L_STRAT = 0.0

    # Reference altitudes
    H_TROPOPAUSE = 11_000
    H_STRATOPAUSE = 20_000

    # Conversions
    FT_TO_M = 0.3048
    M_TO_FT = 1 / FT_TO_M
    KTS_TO_MPS = 0.514444
    MPS_TO_KTS = 1 / KTS_TO_MPS
    NM_TO_KM = 1852
    KM_TO_NM = 1 / NM_TO_KM


    # Air viscosity (Sutherland)
    MU_0 = 1.7894e-5
    T_S = 110.4

    # Derived
    BETA = 1 / T_0
    RHO_SLUGS = RHO_0 / 14.5939

    @classmethod
    def mu(cls, T):
        """Dynamic viscosity at temperature T [K] using Sutherland's law"""
        return cls.MU_0 * (T / cls.T_0)**1.5 * (cls.T_0 + cls.T_S) / (T + cls.T_S)

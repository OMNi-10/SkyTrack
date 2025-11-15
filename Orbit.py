
def is_valid_INC(inc : float) -> bool:
    return 0 <= inc < 180

def is_valid_RAN(ran : float) -> bool:
    return 0 <= ran < 360

def is_valid_ECC(ecc : float) -> bool:
    return 0 <= ecc

def is_valid_AoP(aop : float) -> bool:
    return 0 <= aop < 360

def is_valid_MAn(man : float) -> bool:
    return 0 <= man < 360

class Orbit:
    _useRads : bool  #TODO: Implement radian conversion
    _eps : float = 1e-6

    _INC : float  # degrees
    _RAN : float  # degrees, ECI from vernal point
    _ECC : float
    _AoP : float  # degrees
    _MAn : float  # degrees

    # Setters:
    # setINC
    # setRAN
    # setECC
    # setAOP
    # setMAn

    # Getters:
    def isValid(self):
        return (
            is_valid_INC(self._INC) and
            is_valid_RAN(self._RAN) and
            is_valid_ECC(self._ECC) and
            is_valid_AoP(self._AoP) and
            is_valid_MAn(self._MAn)
        )


    @property
    def INC(self) -> float:
        """
        :return: inclination
        """
        return self._INC

    @property
    def RAN(self) -> float:
        """
        :return: right ascension of the ascending node
        """
        return self._RAN

    @property
    def ECC(self) -> float:
        """
        :return: eccentricity
        """
        return self._ECC

    @property
    def AoP(self) -> float:
        """
        :return: argument of periapsis
        """
        return self.AoP

    @property
    def MAn(self) -> float:
        """
        :return: mean anomaly
        """
        return self._MAn

    @property
    def TAn(self) -> float:
        """
        :return: true anomaly
        """
        # TODO: Implement this method.
        return None

    # Orbit Classification:
    def isCircular(self, eps=None):
        if eps is None:
            eps = self._eps
        return self._ECC <= eps

    def isElliptical(self):
        return 0 < self._ECC < 1

    def isParabolic(self, eps=None):
        if eps is None:
            eps = self._eps
        return abs(self._ECC - 1) <= eps

    def isHyperbolic(self):
        return self._ECC > 1

    # Read in TLE
class int(int):
    def clamp(self, min:int|float, max:int|float)->int|float:
        """Returns value clamped to the inclusive range of min and max
        min: The lower bound of the result.
        max: The upper bound of the result.
        """
        return min if self < min else max if self > max else self

class float(float):
    def clamp(self, min:int|float, max:int|float)->int|float:
        """Returns value clamped to the inclusive range of min and max
        min: The lower bound of the result.
        max: The upper bound of the result.
        """
        return min if self < min else max if self > max else self

    def to_int(self)->int:
        """Safely convert float to int"""
        if int(self)==self:
            return int(self)
        else: raise ValueError(f"Converting {self} to int will result in loss of data")

class str(str):
    def split_by_length(self, length:int)->list:
        """Split a string to list of strings of specified length
        length: desired length of strings split"""
        return [ self[i:i+length] for i in range(0, len(self), length) ]

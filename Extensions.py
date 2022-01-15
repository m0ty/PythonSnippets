class int(int):
    def clamp(self, min:int|float, max:int|float)->int|float:
        """Returns value clamped to the inclusive range of min and max
        min: The lower bound of the result.
        max: The upper bound of the result.
        """
        return min if self < min else max if self > max else self

    def check_bit_at_position(self, position:int)->int:
        """Check bit status at specified position.
        Bits are counted from right to left.
        position: index of bit to check.
        """
        state : bool = self & (1 << position) !=0
        return 1 if state else 0

    def flip_bit_at_position(self, position:int)->int:
        """Flip bit at specified position.
        position: index of bit to flip.
        """
        self ^= (1 << position)
        return self

    def set_bit_at_position(self, position:int, new_value:int)->int:
        """Set bit value at specified position to 0 or 1.
        position: index of bit to set.
        new_value: new value of selected bit. Can be either 0 or 1.
        """
        if new_value not in [0,1]: raise ValueError("new_value parameter must be either 0 or 1")
        mask = 1 << position
        return (self & ~mask) | ((new_value << position) & mask)

    def get_bit_string(self, desired_length:int=0)->str:
        """Return bit value of a integer as string.
        desired_length: length of returned string. Will be filled with zeros.
        """
        return bin(self)[2:].zfill(desired_length)

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

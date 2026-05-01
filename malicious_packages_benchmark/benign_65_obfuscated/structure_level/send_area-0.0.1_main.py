from math import pi, sqrt
if False:
    _var_49_0 = (25, 762, 309)

    def _var_49_fn():
        pass

class Calculate:

    def circle(self, radius):
        return round(radius * pi, 2)

    def triangle(self, a, b, c):
        p = (a + b + c) // 2
        res = sqrt(p * (p - a) * (p - b) * (p - c))
        if False:
            _var_46_0 = (960, 846, 274)
            _var_46_1 = (359, 426, 841)
            _var_46_2 = (125, 314, 139)

            def _var_46_fn():
                pass
        is_rectangular = False
        for a in range(3):
            for b in range(3):
                for c in range(3):
                    if a ** 2 == b ** 2 + c ** 2:
                        is_rectangular = True
                    else:
                        continue
        print(is_rectangular)
        if False:
            _var_47_0 = (65, 480, 47)

            def _var_47_fn():
                pass
        return res
        if False:
            _var_48_0 = (109, 111, 618)
            _var_48_1 = (178, 793, 483)

            def _var_48_fn():
                pass
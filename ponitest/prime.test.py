import prime

class Test_Prime_Prime:
    def test_prime_1(self):
        result = prime.prime(2)
        assert result == True

    def test_prime_2(self):
        result = prime.prime(10)
        assert result == False

    def test_prime_3(self):
        result = prime.prime(-10)
        assert result == False

    def test_prime_4(self):
        result = prime.prime(0.0)
        assert result == False

    def test_prime_5(self):
        result = prime.prime(0)
        assert result == False

    def test_prime_6(self):
        result = prime.prime(-1)
        assert result == False

    def test_prime_7(self):
        result = prime.prime(-5.48)
        assert result == False

    def test_prime_8(self):
        result = prime.prime(100)
        assert result == False

    def test_prime_9(self):
        result = prime.prime(-100)
        assert result == False

    def test_prime_10(self):
        result = prime.prime(-11)
        assert result == False

    def test_prime_11(self):
        result = prime.prime(11)
        assert result == True

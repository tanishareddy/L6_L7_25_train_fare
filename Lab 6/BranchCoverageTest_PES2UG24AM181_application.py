
import pytest
from train_fare import base_fare, concession, tatkal_charge


# ---------------- BASE FARE TESTS ----------------

def test_sleeper_fare():
    assert base_fare("SL", 500) == 500

def test_all_travel_classes():
    assert base_fare("3A", 100) == 200
    assert base_fare("2A", 100) == 300
    assert base_fare("1A", 100) == 500

def test_minimum_fare():
    assert base_fare("SL", 10) == 50

def test_fare_above_minimum():
    assert base_fare("SL", 100) == 100

def test_invalid_travel_class():
    with pytest.raises(ValueError, match="unknown class"):
        base_fare("AC", 100)

def test_invalid_distance_zero():
    with pytest.raises(ValueError, match="invalid distance"):
        base_fare("SL", 0)

def test_invalid_distance_negative():
    with pytest.raises(ValueError, match="invalid distance"):
        base_fare("SL", -10)


# ---------------- CONCESSION TESTS ----------------

def test_tatkal_no_concession():
    assert concession(3, "F", True) == 0

def test_child_below_five():
    assert concession(4, "M", False) == 100

def test_child_age_five():
    assert concession(5, "M", False) == 50

def test_child_age_twelve():
    assert concession(12, "F", False) == 50

def test_adult_no_concession():
    assert concession(30, "M", False) == 0

def test_senior_female_concession():
    assert concession(60, "F", False) == 50

def test_senior_male_concession():
    assert concession(60, "M", False) == 40


# ---------------- TATKAL CHARGE TESTS ----------------

def test_sleeper_tatkal_charge():
    assert tatkal_charge("SL", 500) == 100

def test_other_class_tatkal_charge():
    assert tatkal_charge("3A", 500) == 150

def test_tatkal_charge_below_minimum():
    assert tatkal_charge("SL", 500) == 100

def test_tatkal_charge_above_maximum():
    assert tatkal_charge("3A", 2000) == 400

def test_tatkal_charge_at_minimum_boundary():
    assert tatkal_charge("SL", 1000) == 100

def test_tatkal_charge_at_maximum_boundary():
    assert tatkal_charge("3A", 4000) == 400

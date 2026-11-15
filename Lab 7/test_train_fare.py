
import pytest
from hypothesis import given, strategies as st

from train_fare import parse_pnr, journey_distance, berth_type


# -------------------------------------------------
# 1. PNR PARSING TESTS
# -------------------------------------------------

@given(st.text(alphabet="0123456789", min_size=10, max_size=10))
def test_parse_pnr_valid(pnr):
    zone, number = parse_pnr(pnr)
    assert zone == int(pnr[0])
    assert number == int(pnr[1:])


@given(
    st.one_of(
        st.none(),
        st.just(""),
        st.text(alphabet="0123456789", max_size=9),
        st.text(alphabet="0123456789", min_size=11, max_size=20),
        st.text(alphabet="abcdef", min_size=1)
    )
)
def test_parse_pnr_invalid(pnr):
    with pytest.raises(ValueError):
        parse_pnr(pnr)


# -------------------------------------------------
# 2. JOURNEY DISTANCE TESTS
# -------------------------------------------------

@given(
    st.lists(
        st.integers(min_value=0, max_value=100000),
        min_size=2,
        max_size=20
    )
)
def test_journey_distance_valid(distances):
    csv_input = ",".join(map(str, distances))
    result = journey_distance(csv_input)
    assert result == distances[-1] - distances[0]


@given(
    st.one_of(
        st.none(),
        st.just(""),
        st.just("100"),
        st.just("1,,3"),
        st.just("1,abc,3"),
        st.text(alphabet="abcdef", min_size=1)
    )
)
def test_journey_distance_invalid(distances):
    with pytest.raises(ValueError):
        journey_distance(distances)


# -------------------------------------------------
# 3. BERTH TYPE TESTS
# -------------------------------------------------

@given(
    st.text(alphabet="ABCDEFGHIJKLMNOPQRSTUVWXYZ", min_size=1, max_size=5),
    st.integers(min_value=1, max_value=100000)
)
def test_berth_type_valid(coach, seat):
    result = berth_type(f"{coach}-{seat}")
    assert result[0] == coach.upper()
    assert result[1] in ["SU", "LB", "MB", "UB", "SL"]


@given(
    st.one_of(
        st.none(),
        st.just(""),
        st.just("S3"),
        st.just("-45"),
        st.just("S3-"),
        st.just("S3-abc"),
        st.just("S3-0"),
        st.just("S3--1"),
        st.just("S3-1-extra")
    )
)
def test_berth_type_invalid(seat):
    with pytest.raises(ValueError):
        berth_type(seat)

import EvenorOdd
import pytest
@pytest.mark.parametrize("a,res",[(2,True),(3,False),(5,True),(8,True),(10,False),(11,True),(17,False)])
def test_check_evenorodd(a,res):
    result=EvenorOdd.Check_Evenorodd(a)
    assert result==res
"""
This module lets you practice the ACCUMULATOR pattern
in its simplest classic forms:
   SUMMING:       total = total + number

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and mohammed.
"""  # TODOdone: 1. PUT YOUR NAME IN THE ABOVE LINE.
import math

def main():
    """ Calls the   TEST   functions in this module. """
    run_test_sum_cosines()
    run_test_sum_square_roots()


def run_test_sum_cosines():
    """ Tests the   sum_cosines   function. """
    # ------------------------------------------------------------------
    # TODO: 2. Implement this function.
    #   It TESTS the  sum_cosines  function defined below.
    #   Include at least **   3   ** tests.
    #
    # Use the same 4-step process as in implementing previous
    # TEST functions, including the same way to print expected/actual.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_cosines   function:')
    print('--------------------------------------------------')

    expected = 1.54
    answer = math.cos(0) + math.cos(1)
    print('Test 1 expected:', expected)
    print('         actual:', answer)

    expected2 = 1.12
    answer2 = math.cos(0) + math.cos(1) + math.cos(2)
    print('Test 2 expected:', expected2)
    print('         actual:', answer2)

    expected3 = .134
    answer3 = math.cos(0) + math.cos(1) + math.cos(2) + math.cos(3)
    print('Test 3 expected:', expected3)
    print('         actual:', answer3)


def sum_cosines(n):
    """
    What comes in:  A non-negative integer n.
    What goes out:  The sum of the cosines of the integers
       0, 1, 2, 3, ... n, inclusive, for the given n.
    Side effects:   None.
    Example:
      If n is 3, this function returns
        cos(0) + cos(1) + cos(2) + cos(3)   which is about 0.13416.
    """
    # ------------------------------------------------------------------
    # TOdoneDO: 3. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #   That is called TEST-DRIVEN DEVELOPMENT (TDD).
    #
    #   No fair running the code of  sum_cosines  to GENERATE
    #   test cases; that would defeat the purpose of TESTING!
    # ------------------------------------------------------------------

    total = 0
    for k in range(n):
            total = total + cos(k)

            return total


def run_test_sum_square_roots():
    """ Tests the   sum_square_roots   function. """
    # ------------------------------------------------------------------
    # TdoneODO: 4. Implement this function.
    #   It TESTS the  sum_square_roots  function defined below.
    #   Include at least **   3   ** tests.
    #
    # Use the same 4-step process as in implementing previous
    # TEST functions, including the same way to print expected/actual.
    # ------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_square_roots   function:')
    print('--------------------------------------------------')

    expected = 8.7
    answer = math.sqrt(2) + math.sqrt(4) + math.sqrt(6) + math.sqrt(8)
    print('Test 1 expected:', expected)
    print('         actual:', answer)

    expected2 = 11.9
    answer2 =math. sqrt(2) + math.sqrt(4) + math.sqrt(6) + math.sqrt(8) + math.sqrt(10)
    print('Test 2 expected:', expected2)
    print('         actual:', answer2)

    expected3 = 15.3
    answer3 = math.sqrt(2) + math.sqrt(4) + math.sqrt(6) + math.sqrt(8) + math.sqrt(10) + math.sqrt(12)
    print('Test 3 expected:', expected3)
    print('         actual:', answer3)

def sum_square_roots(n):
    """
    What comes in:  A non-negative integer n.
    What goes out:  The sum of the square roots of the integers
       2, 4, 6, 8, ... 2n    inclusive, for the given n.
           So if n is 7, the last term of the sum is
           the square root of 14 (not 7).
    Side effects:   None.
    Example:
      If n is 5, this function returns
         sqrt(2) + sqrt(4) + sqrt(6) + sqrt(8) + sqrt(10),
      which is about 11.854408.
    """
    # ------------------------------------------------------------------
    # TODdoneO: 5. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #   That is called TEST-DRIVEN DEVELOPMENT (TDD).
    #
    #   No fair running the code of  sum_square_roots  to GENERATE
    #   test cases; that would defeat the purpose of TESTING!
    # ------------------------------------------------------------------

    total = 0
    for k in range(n):
            total = total + math.sqrt(k)

            return total
# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()

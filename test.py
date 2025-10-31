import math
# --- Imports with dummy fallback ---
try:
    from q1 import distance
except:
    print('q1a import failed')
    distance = lambda *a: None

try:
    from q1 import area_from_sides
except:
    print('q1b import failed')
    area_from_sides = lambda *a: None

try:
    from q1 import area_from_vertices
except:
    print('q1c import failed')
    area_from_vertices = lambda *a: None

try:
    from q2 import convert_temperature
except:
    print('q2 import failed')
    convert_temperature = lambda *a: 1000000


try:
    from q0 import solve_quadratic
except:
    print('q0 import failed')
    solve_quadratic = lambda *a: None

# --- Helper ---
def is_close(x, y):
    try:
        return math.isclose(float(x), float(y), rel_tol=1e-9, abs_tol=1e-6)
    except Exception:
        return False

# --- Individual test wrappers with expected values ---
def test_q1a_1(): return distance(-2, -2, -2, -2), 0
def test_q1a_2(): return distance(3, 5, 9, 13), 10
def test_q1a_3(): return distance(0, 3, 4, 0), 5

def test_q1b_1(): return area_from_sides(6.25, 4.25, 6.5), 12.75
def test_q1b_2(): return area_from_sides(20.5, 20.5, 9), 90
def test_q1b_3(): return area_from_sides(14.32, 18.53, 5.612), 30.027385522357424

def test_q1c_1(): return area_from_vertices(0, 0, 3, 0, 0, 4), 6
def test_q1c_2(): return area_from_vertices(-5, 0, 5, 0, 0, 5), 25
def test_q1c_3(): return area_from_vertices(-4, 0, 4, 0, 4, 4), 16

def test_q2_1(): return convert_temperature(100, "C"), 212
def test_q2_2(): return convert_temperature(212, "F"), 100
def test_q2_3(): return convert_temperature(212, "K"), None
def test_q2_4(): return convert_temperature(32, "F"), 0
def test_q2_5(): return convert_temperature(-40, "F"), -40
def test_q2_6(): return convert_temperature(-40, "C"), -40


def test_q0_1(): return solve_quadratic(1, -5, 6), 2
def test_q0_2(): return solve_quadratic(5, -33, 50.4), 2.4
def test_q0_3(): return solve_quadratic(2, 25, 75), -7.5

tests = {
    'q0':  [test_q0_1, test_q0_2, test_q0_3],
    'q1a': [test_q1a_1, test_q1a_2, test_q1a_3],
    'q1b': [test_q1b_1, test_q1b_2, test_q1b_3],
    'q1c': [test_q1c_1, test_q1c_2, test_q1c_3],
    'q2':  [test_q2_1, test_q2_2, test_q2_3, test_q2_4, test_q2_5, test_q2_6],
}

passed = {k: 0 for k in tests.keys()}
failures = {k: [] for k in tests.keys()}

# --- Colors ---
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
BOLD = "\033[1m"
END = "\033[0m"

if __name__ == '__main__':
    for k in tests:
        for test in tests[k]:
            try:
                got, expected = test()
                # Special case for None expected
                if expected is None:
                    ok = (got is None)
                else:
                    ok = is_close(got, expected)
                if ok:
                    passed[k] += 1
                else:
                    failures[k].append((test.__name__, expected, got))
            except Exception as e:
                failures[k].append((test.__name__, "?", f"ERROR: {e}"))

        total = len(tests[k])
        score = passed[k]
        if score == total:
            color = GREEN
        elif score == 0:
            color = RED
        else:
            color = YELLOW
        print(f"{color}Question {k}: {score}/{total} Tests Passed{END}")
        for name, expected, got in failures[k]:
            print(f"  {RED}- FAIL: {name} | expected: {expected} got: {got}{END}")

    overall_score = sum(passed.values())
    overall_total = sum(len(v) for v in tests.values())
    overall_color = GREEN if overall_score == overall_total else (YELLOW if overall_score > 0 else RED)
    print(f"{overall_color}{BOLD}Overall: {overall_score}/{overall_total} Tests Passed{END}")

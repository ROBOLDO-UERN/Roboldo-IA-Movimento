from movimento_slam.path_planner import Pose2D, compute_distance


def test_compute_distance():
    p1 = Pose2D(0.0, 0.0)
    p2 = Pose2D(3.0, 4.0)
    assert compute_distance(p1, p2) == (3.0, 4.0)

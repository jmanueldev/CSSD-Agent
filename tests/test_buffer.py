from cssd.memory.buffer import TrajectoryBuffer

def test_buffer():
    buf = TrajectoryBuffer(2)
    buf.add(1)
    buf.add(2)
    buf.add(3)

    assert len(buf.buffer) == 2

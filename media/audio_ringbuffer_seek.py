import math

def advance(ptr, n, capacity):
    """环形推进。"""
    raise NotImplementedError("TODO: advance")

def readable(start, end, capacity):
    """可读帧数。"""
    raise NotImplementedError("TODO: readable")

def seek_flag(pos, duration):
    """seek 触发。"""
    raise NotImplementedError("TODO: seek_flag")

def reset_decoder(state):
    """清解码器。"""
    raise NotImplementedError("TODO: reset_decoder")

def version_key(task, version):
    """预取版本键。"""
    raise NotImplementedError("TODO: version_key")

def frame_bytes(channels, bytes_per_sample):
    """帧字节。"""
    raise NotImplementedError("TODO: frame_bytes")

def reset_clock(pos):
    """时钟重置。"""
    raise NotImplementedError("TODO: reset_clock")

def pad_tail(frames, need):
    """尾帧补齐。"""
    raise NotImplementedError("TODO: pad_tail")

def is_silence(frame):
    """静音帧判定。"""
    raise NotImplementedError("TODO: is_silence")

def copy_frame(src, channels):
    """按帧拷贝。"""
    raise NotImplementedError("TODO: copy_frame")

def capacity(frames, frame_size):
    """缓冲容量。"""
    raise NotImplementedError("TODO: capacity")

def wrap_dist(a, b, capacity):
    """回绕距离。"""
    raise NotImplementedError("TODO: wrap_dist")

def valid_ptr(ptr, capacity):
    """指针有效。"""
    raise NotImplementedError("TODO: valid_ptr")

def seek_target(pos, duration):
    """seek 目标。"""
    raise NotImplementedError("TODO: seek_target")

def buffer_key(reader_id):
    """缓冲键。"""
    raise NotImplementedError("TODO: buffer_key")

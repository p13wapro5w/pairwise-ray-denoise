"""第 55 批：光追反射一移动就拖尾、毛发边缘糊、暗部噪点像油画..."""

def spatial_weight(distance):
    """返回空间降噪权重。"""
    raise NotImplementedError("TODO: spatial_weight")

def temporal_alpha(frame_count, max_frames):
    """返回时间累积系数。"""
    raise NotImplementedError("TODO: temporal_alpha")

def guide_weight(normal_diff, depth_diff):
    """返回法线与深度引导权重。"""
    raise NotImplementedError("TODO: guide_weight")

def ray_length_weight(length):
    """按反射光线长度返回权重。"""
    raise NotImplementedError("TODO: ray_length_weight")

def protect_highlight(value, threshold):
    """保护高光不被模糊。"""
    raise NotImplementedError("TODO: protect_highlight")

def reset_on_motion(motion):
    """运动物体重置历史。"""
    raise NotImplementedError("TODO: reset_on_motion")

def upsample_reflection(center_depth, neighbor_depth):
    """深度感知反射上采样。"""
    raise NotImplementedError("TODO: upsample_reflection")

def adaptive_samples(variance):
    """按方差返回采样数。"""
    raise NotImplementedError("TODO: adaptive_samples")

def linear_space(value):
    """在线性空间做降噪。"""
    raise NotImplementedError("TODO: linear_space")

def stereo_denoise(view_id):
    """按眼别返回独立降噪历史。"""
    raise NotImplementedError("TODO: stereo_denoise")

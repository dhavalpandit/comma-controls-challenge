from . import BaseController
import numpy as np


class Controller(BaseController):
  def __init__(self):
    self.p = 0.195
    self.i = 0.100
    self.d = -0.053

    self.error_integral = 0.0
    self.prev_error = 0.0

  def update(self, target_lataccel, current_lataccel, state, future_plan):
    error = target_lataccel - current_lataccel
    self.error_integral += error
    self.error_integral = float(np.clip(self.error_integral, -40.0, 40.0))

    error_diff = error - self.prev_error
    self.prev_error = error

    preview_term = 0.0
    if future_plan is not None and len(future_plan.lataccel) >= 10:
      weights = np.array([10,9,8,7,6,5,4,3,2,1], dtype=float)
      weights = weights / weights.sum()
      future_target = np.sum(np.array(future_plan.lataccel[:10]) * weights)
      preview_term = 0.025 * (future_target - target_lataccel)

    action = (
      self.p * error
      + self.i * self.error_integral
      + self.d * error_diff
      + preview_term
    )

    return float(np.clip(action, -2.0, 2.0))

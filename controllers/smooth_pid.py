from . import BaseController
import numpy as np


class Controller(BaseController):
  """
  PID-based controller close to the stock PID, with safe integral clipping.
  Goal: keep tracking accuracy strong before adding advanced lookahead.
  """

  def __init__(self):
    self.kp = 0.195
    self.ki = 0.100
    self.kd = -0.053
    self.kff = 0.0

    self.error_integral = 0.0
    self.prev_error = 0.0

    self.max_integral = 40.0
    self.max_action = 2.0

  def update(self, target_lataccel, current_lataccel, state, future_plan):
    error = target_lataccel - current_lataccel

    self.error_integral += error
    self.error_integral = float(np.clip(
      self.error_integral,
      -self.max_integral,
      self.max_integral
    ))

    error_diff = error - self.prev_error
    self.prev_error = error

    speed_gain = 1.0

    action = (
      speed_gain * (
        self.kp * error
        + self.ki * self.error_integral
        + self.kd * error_diff
      )
      + self.kff * target_lataccel
    )

    action = float(np.clip(action, -self.max_action, self.max_action))
    return action

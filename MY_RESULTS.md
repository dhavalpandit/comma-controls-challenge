# Comma.ai Controls Challenge – Controller Development Journey

## Author
Dhaval Pandit

## Objective

The goal of this project was to improve the baseline controller provided in the comma.ai Controls Challenge by leveraging future trajectory information and systematic controller tuning.

## Environment

- Python 3.12
- NumPy
- Pandas
- ONNX Runtime
- TinyPhysics Simulator

## Baseline Results

| Controller | Total Cost |
|------------|------------|
| PID (Provided Baseline) | 84.85 |

## Controller Evolution

### Preview PID V1
Score: 84.67

### Preview PID V2
Score: 84.57

### Preview PID V3
Score: 84.15

### Preview PID V4 (Best Result)
Score: 84.02

## Improvement Summary

| Version | Score |
|----------|--------|
| Baseline PID | 84.85 |
| Preview PID V1 | 84.67 |
| Preview PID V2 | 84.57 |
| Preview PID V3 | 84.15 |
| Preview PID V4 | 84.02 |

Total Improvement:

84.85 → 84.02

## Key Learnings

- Future trajectory information improves controller performance.
- Weighted trajectory preview outperformed single-point preview.
- Tracking accuracy has a larger effect on total cost than jerk reduction.
- Small controller modifications can produce measurable gains.

## Future Work

- Model Predictive Control (MPC)
- Action sequence optimization
- TinyPhysics model-based planning
- Reinforcement Learning approaches

## Repository Structure

- best_pid_preview.py
- preview_pid.py
- preview_pid_v2.py
- preview_pid_v3.py
- preview_pid_v4.py
- smooth_pid.py

## Best Result

Preview PID V4: 84.02

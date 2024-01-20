import numpy as np
import matplotlib.pyplot as plt

# 加载HighD测试数据
HighD_data = np.load('D:\Projects\FollowNet-car\data\HighD_car_fol_event_set_dhw.npy')

print(HighD_data)

Ts = 0.04

for num in range(1):
    spacing, svSpd_obs, relspeed, lvSpd_obs = HighD_data[num][0], HighD_data[num][1], HighD_data[num][2], HighD_data[num][3]

    plt.figure()  #
    plt.subplot(2, 1, 1)  #
    plt.plot(lvSpd_obs, label='LV')
    plt.plot(svSpd_obs, label='SV ')
    # plt.plot(relspeed, label='Relative_speed')
    plt.legend()
    # plt.ylim([0, 30])
    plt.xlabel(f'Time step ({Ts}s as sample interval)')
    plt.ylabel('Speed (m/s)')
    plt.subplot(2, 1, 2)
    plt.plot(spacing, label='spacing_GoundTruth')

    plt.legend()
    plt.xlabel('Time step (0.04s as sample interval)')
    plt.ylabel('Spacing (m)')
    plt.show()
    
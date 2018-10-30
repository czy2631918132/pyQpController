import sys
import numpy as np

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
from matplotlib.font_manager import FontProperties



if __name__ =="__main__":

    fileName =  sys.argv[1]
    loaded = np.load(fileName)

    impactFileName = sys.argv[2]
    impact_loaded = np.load(impactFileName)

    #loaded = np.load("../log/data/data_Oct_23_2018_20-53-13.npz")
    #impact_loaded = np.load("../log/data/impact-data_Oct_23_2018_20-53-13.npz")

    time = loaded['time']

    error_x = loaded['error'][:, 0]
    error_y = loaded['error'][:, 1]
    error_z = loaded['error'][:, 2]

    fontP = FontProperties()
    fontP.set_size('small')



    #fig1, (ax11, ax12, ax13 )= plt.subplots(nrows=3, ncols=1)
    # ax1 = plt.subplot(311)
    # plt.plot(time, error_x, label='error x')
    # ax11.set_ylabel('error x')
    #
    # ax12 = plt.subplot(312)
    # plt.plot(time, error_y, label='error y')
    # ax12.set_ylabel('error y')
    #
    # ax13 = plt.subplot(313)
    # plt.plot(time, error_z, label='error z')
    # plt.ylabel('error z')
    # plt.grid(True)
    # plt.xlabel('Time [s]')

    fig12 = plt.figure()

    impact_time_1 = [1.80, 1.85]
    impact_time_2 = [3.42, 3.45]
    impact_time_3 = [3.94, 4.02]



    ax = fig12.gca()
    ax.plot(time, error_x, label='Error x')
    # plt.axvspan(impact_time_1[0], impact_time_1[1], color='red', alpha=0.1)
    # plt.axvspan(impact_time_2[0], impact_time_2[1], color='red', alpha=0.1)
    # plt.axvspan(impact_time_3[0], impact_time_3[1], color='red', alpha=0.1)
    ax.plot(time, error_y, label='Error y')
    ax.plot(time, error_z, label='Error z')
    ax.legend(prop=fontP)
    plt.xlabel('Time [s]')
    plt.ylabel('Task Error')
    plt.title('End-effector velocity Task')
    plt.grid(True)
    fig12.savefig("task_error.pdf", bbox_inches='tight')

    dq_0 = loaded['dq'][:, 0]
    dq_1 = loaded['dq'][:, 1]
    dq_2 = loaded['dq'][:, 2]
    dq_3 = loaded['dq'][:, 3]
    dq_4 = loaded['dq'][:, 4]
    dq_5 = loaded['dq'][:, 5]

    impact_time = impact_loaded['time']
    predict_delta_dq_0 = impact_loaded['predict_delta_dq'][:,0]
    predict_delta_dq_1 = impact_loaded['predict_delta_dq'][:,1]
    predict_delta_dq_2 = impact_loaded['predict_delta_dq'][:,2]
    predict_delta_dq_3 = impact_loaded['predict_delta_dq'][:,3]
    predict_delta_dq_4 = impact_loaded['predict_delta_dq'][:,4]
    predict_delta_dq_5 = impact_loaded['predict_delta_dq'][:,5]

    actual_delta_dq_0 = impact_loaded['actual_delta_dq'][:, 0]
    actual_delta_dq_1 = impact_loaded['actual_delta_dq'][:, 1]
    actual_delta_dq_2 = impact_loaded['actual_delta_dq'][:, 2]
    actual_delta_dq_3 = impact_loaded['actual_delta_dq'][:, 3]
    actual_delta_dq_4 = impact_loaded['actual_delta_dq'][:, 4]
    actual_delta_dq_5 = impact_loaded['actual_delta_dq'][:, 5]

    predict_delta_torque_0 = impact_loaded['predict_delta_tau'][:,0]
    predict_delta_torque_1 = impact_loaded['predict_delta_tau'][:,1]
    predict_delta_torque_2 = impact_loaded['predict_delta_tau'][:,2]
    predict_delta_torque_3 = impact_loaded['predict_delta_tau'][:,3]
    predict_delta_torque_4 = impact_loaded['predict_delta_tau'][:,4]
    predict_delta_torque_5 = impact_loaded['predict_delta_tau'][:,5]

    actual_delta_torque_0 = impact_loaded['actual_delta_tau'][:, 0]
    actual_delta_torque_1 = impact_loaded['actual_delta_tau'][:, 1]
    actual_delta_torque_2 = impact_loaded['actual_delta_tau'][:, 2]
    actual_delta_torque_3 = impact_loaded['actual_delta_tau'][:, 3]
    actual_delta_torque_4 = impact_loaded['actual_delta_tau'][:, 4]
    actual_delta_torque_5 = impact_loaded['actual_delta_tau'][:, 5]

    predict_F_0 = impact_loaded['predict_F'][:, 0]
    predict_F_1 = impact_loaded['predict_F'][:, 1]
    predict_F_2 = impact_loaded['predict_F'][:, 2]

    actual_F_0 = impact_loaded['actual_F'][:, 0]
    actual_F_1 = impact_loaded['actual_F'][:, 1]
    actual_F_2 = impact_loaded['actual_F'][:, 2]





    fig2, (ax21, ax22, ax23, ax24, ax25, ax26) = plt.subplots(nrows=6, ncols=1)

    ax21 = plt.subplot(611)
    plt.plot(time, dq_0, label='dq')
    ax21.set_ylabel('dq 0')
    ax21.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    plt.plot(impact_time, predict_delta_dq_0, label='Predicted delta dq')
    # plt.axvspan(impact_time_1[0], impact_time_1[1], color='red', alpha=0.1)
    # plt.axvspan(impact_time_2[0], impact_time_2[1], color='red', alpha=0.1)
    # plt.axvspan(impact_time_3[0], impact_time_3[1], color='red', alpha=0.1)
    plt.setp(ax21.get_xticklabels(), visible=False)
    plt.plot(impact_time, actual_delta_dq_0, label='Actual delta dq')
    ax21.locator_params(nbins=5, axis='y')

    plt.grid(True)
    ax21.legend(prop=fontP)
    plt.title("Joint velocities and joint velocities jump at the impact time")

    ax22 = plt.subplot(612)
    plt.plot(time, dq_1)
    plt.plot(impact_time, predict_delta_dq_1)
    plt.plot(impact_time, actual_delta_dq_1)
    # plt.axvspan(impact_time_1[0], impact_time_1[1], color='red', alpha=0.1)
    # plt.axvspan(impact_time_2[0], impact_time_2[1], color='red', alpha=0.1)
    # plt.axvspan(impact_time_3[0], impact_time_3[1], color='red', alpha=0.1)
    ax22.set_ylabel('dq 1')
    ax22.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    plt.setp(ax22.get_xticklabels(), visible=False)
    plt.grid(True)
    ax22.legend()
    ax22.locator_params(nbins=5, axis='y')

    ax23 = plt.subplot(613)
    plt.plot(time, dq_2)
    plt.plot(impact_time, predict_delta_dq_2)
    plt.plot(impact_time, actual_delta_dq_2)
    # plt.axvspan(impact_time_1[0], impact_time_1[1], color='red', alpha=0.1)
    # plt.axvspan(impact_time_2[0], impact_time_2[1], color='red', alpha=0.1)
    # plt.axvspan(impact_time_3[0], impact_time_3[1], color='red', alpha=0.1)
    ax23.set_ylabel('dq 2')
    ax23.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    plt.setp(ax23.get_xticklabels(), visible=False)
    plt.grid(True)
    ax23.legend()
    ax23.locator_params(nbins=5, axis='y')

    ax24 = plt.subplot(614)
    plt.plot(time, dq_3)
    plt.plot(impact_time, predict_delta_dq_3)
    plt.plot(impact_time, actual_delta_dq_3)
    # plt.axvspan(impact_time_1[0], impact_time_1[1], color='red', alpha=0.1)
    # plt.axvspan(impact_time_2[0], impact_time_2[1], color='red', alpha=0.1)
    # plt.axvspan(impact_time_3[0], impact_time_3[1], color='red', alpha=0.1)
    ax24.set_ylabel('dq 3')
    plt.setp(ax24.get_xticklabels(), visible=False)
    ax24.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))

    plt.grid(True)
    ax24.legend()
    ax24.locator_params(nbins=5, axis='y')

    ax25 = plt.subplot(615)
    plt.plot(time, dq_4)
    plt.plot(impact_time, predict_delta_dq_4)
    plt.plot(impact_time, actual_delta_dq_4)
    # plt.axvspan(impact_time_1[0], impact_time_1[1], color='red', alpha=0.1)
    # plt.axvspan(impact_time_2[0], impact_time_2[1], color='red', alpha=0.1)
    # plt.axvspan(impact_time_3[0], impact_time_3[1], color='red', alpha=0.1)
    ax25.set_ylabel('dq 4')
    plt.setp(ax25.get_xticklabels(), visible=False)
    ax25.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    plt.grid(True)
    ax25.legend()
    ax25.locator_params(nbins=5, axis='y')

    ax26 = plt.subplot(616)
    plt.plot(time, dq_5)
    plt.plot(impact_time, predict_delta_dq_5)
    plt.plot(impact_time, actual_delta_dq_5)
    # plt.axvspan(impact_time_1[0], impact_time_1[1], color='red', alpha=0.1)
    # plt.axvspan(impact_time_2[0], impact_time_2[1], color='red', alpha=0.1)
    # plt.axvspan(impact_time_3[0], impact_time_3[1], color='red', alpha=0.1)
    ax26.set_ylabel('dq 5')
    plt.xlabel('Time [s]')
    plt.grid(True)
    ax26.legend()
    ax26.locator_params(nbins=5, axis='y')
    ax26.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    fig2.savefig("Delta_dq.pdf", bbox_inches='tight')

    fig3, (ax31, ax32, ax33, ax34, ax35, ax36) = plt.subplots(nrows=6, ncols=1)

    ax31 = plt.subplot(611)
    ax31.set_ylabel('Joint 0')
    plt.plot(impact_time, predict_delta_torque_0, label='Predicted torque jump')
    plt.plot(impact_time, actual_delta_torque_0, label='Actual torque jump')
    # plt.axvspan(impact_time_1[0], impact_time_1[1], color='red', alpha=0.1)
    # plt.axvspan(impact_time_2[0], impact_time_2[1], color='red', alpha=0.1)
    # plt.axvspan(impact_time_3[0], impact_time_3[1], color='red', alpha=0.1)
    plt.setp(ax31.get_xticklabels(), visible=False)
    plt.grid(True)
    ax31.legend(prop=fontP)
    plt.title("Joint torque jumps at the impact time")
    ax31.locator_params(nbins=5, axis='y')
    ax31.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))

    ax32 = plt.subplot(612)
    plt.plot(impact_time, predict_delta_torque_1)
    plt.plot(impact_time, actual_delta_torque_1)
    # plt.axvspan(impact_time_1[0], impact_time_1[1], color='red', alpha=0.1)
    # plt.axvspan(impact_time_2[0], impact_time_2[1], color='red', alpha=0.1)
    # plt.axvspan(impact_time_3[0], impact_time_3[1], color='red', alpha=0.1)
    ax32.set_ylabel('Joint 1')
    plt.setp(ax32.get_xticklabels(), visible=False)
    ax32.locator_params(nbins=5, axis='y')
    ax32.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    plt.grid(True)
    ax32.legend()

    ax33 = plt.subplot(613)
    plt.plot(impact_time, predict_delta_torque_2)
    plt.plot(impact_time, actual_delta_torque_2)
    # plt.axvspan(impact_time_1[0], impact_time_1[1], color='red', alpha=0.1)
    # plt.axvspan(impact_time_2[0], impact_time_2[1], color='red', alpha=0.1)
    # plt.axvspan(impact_time_3[0], impact_time_3[1], color='red', alpha=0.1)
    ax33.set_ylabel('Joint 2')
    plt.setp(ax33.get_xticklabels(), visible=False)
    ax33.locator_params(nbins=5, axis='y')
    ax33.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    plt.grid(True)
    ax33.legend()

    ax34 = plt.subplot(614)
    plt.plot(impact_time, predict_delta_torque_3)
    plt.plot(impact_time, actual_delta_torque_3)
    # plt.axvspan(impact_time_1[0], impact_time_1[1], color='red', alpha=0.1)
    # plt.axvspan(impact_time_2[0], impact_time_2[1], color='red', alpha=0.1)
    # plt.axvspan(impact_time_3[0], impact_time_3[1], color='red', alpha=0.1)
    ax34.set_ylabel('Joint 3')
    plt.setp(ax34.get_xticklabels(), visible=False)
    ax34.locator_params(nbins=5, axis='y')
    ax34.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    plt.grid(True)
    ax34.legend()

    ax35 = plt.subplot(615)
    plt.plot(impact_time, predict_delta_torque_4)
    plt.plot(impact_time, actual_delta_torque_4)
    # plt.axvspan(impact_time_1[0], impact_time_1[1], color='red', alpha=0.1)
    # plt.axvspan(impact_time_2[0], impact_time_2[1], color='red', alpha=0.1)
    # plt.axvspan(impact_time_3[0], impact_time_3[1], color='red', alpha=0.1)
    ax35.set_ylabel('Joint 4')
    plt.setp(ax35.get_xticklabels(), visible=False)
    ax35.locator_params(nbins=5, axis='y')
    ax35.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    plt.grid(True)
    ax35.legend()

    ax36 = plt.subplot(616)
    plt.plot(impact_time, predict_delta_torque_5)
    plt.plot(impact_time, actual_delta_torque_5)
    # plt.axvspan(impact_time_1[0], impact_time_1[1], color='red', alpha=0.1)
    # plt.axvspan(impact_time_2[0], impact_time_2[1], color='red', alpha=0.1)
    # plt.axvspan(impact_time_3[0], impact_time_3[1], color='red', alpha=0.1)
    ax36.set_ylabel('Joint 5')
    plt.xlabel('Impact Time [s]')
    plt.grid(True)
    ax36.locator_params(nbins=5, axis='y')
    ax36.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    ax36.legend()
    fig3.savefig("Delta_torque.pdf", bbox_inches='tight')

    fig4, (ax41, ax42, ax43 )= plt.subplots(nrows=3, ncols=1)
    ax41 = plt.subplot(311)
    plt.plot(impact_time, predict_F_0, label='Predicted')
    plt.plot(impact_time, actual_F_0, label='Actual')
    # plt.axvspan(impact_time_1[0], impact_time_1[1], color='red', alpha=0.1)
    # plt.axvspan(impact_time_2[0], impact_time_2[1], color='red', alpha=0.1)
    # plt.axvspan(impact_time_3[0], impact_time_3[1], color='red', alpha=0.1)
    plt.setp(ax41.get_xticklabels(), visible=False)
    ax41.locator_params(nbins=5, axis='y')
    ax41.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    plt.grid(True)
    ax41.legend(prop=fontP)
    ax41.set_ylabel('Force x')
    plt.title("Precited contact force Versus measured contact force ")

    ax42 = plt.subplot(312)
    plt.plot(impact_time, predict_F_1)
    plt.plot(impact_time, actual_F_1)
    # plt.axvspan(impact_time_1[0], impact_time_1[1], color='red', alpha=0.1)
    # plt.axvspan(impact_time_2[0], impact_time_2[1], color='red', alpha=0.1)
    # plt.axvspan(impact_time_3[0], impact_time_3[1], color='red', alpha=0.1)
    plt.setp(ax42.get_xticklabels(), visible=False)
    ax42.locator_params(nbins=5, axis='y')
    ax42.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    plt.grid(True)
    ax42.set_ylabel('Force y')

    ax43 = plt.subplot(313)
    plt.plot(impact_time, predict_F_2)
    plt.plot(impact_time, actual_F_2)
    # plt.axvspan(impact_time_1[0], impact_time_1[1], color='red', alpha=0.1)
    # plt.axvspan(impact_time_2[0], impact_time_2[1], color='red', alpha=0.1)
    # plt.axvspan(impact_time_3[0], impact_time_3[1], color='red', alpha=0.1)
    plt.ylabel('Force z')
    plt.grid(True)
    ax43.locator_params(nbins=5, axis='y')
    ax43.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    fig4.savefig("impact_force.pdf", bbox_inches='tight')


    plt.grid(True)
    plt.xlabel('Impact Time [s]')

    plt.show()


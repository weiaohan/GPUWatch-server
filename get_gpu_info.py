# -*- coding: utf-8 -*-
# by Hank 2019/5/30

from pynvml import *
import psutil

def get_gpu_info():
    GPUS = {}
    nvmlInit()
    # 获得驱动信息
    GPUS["driver-info"] = nvmlSystemGetDriverVersion().decode()
    #查看设备
    deviceCount = nvmlDeviceGetCount()
    for i in range(deviceCount):
        handle = nvmlDeviceGetHandleByIndex(i)
        GPU = "GPU" + str(i)
        GPUS[GPU] = {}
        tmp = GPUS[GPU]
        tmp["index"] = i
        info = nvmlDeviceGetMemoryInfo(handle)
        tmp["total"] = info.total / 1048576
        tmp["usage"] = info.used / 1048576
        tmp["free"] = info.free / 1048576

    print(GPUS)
    nvmlShutdown()
    return GPUS

def getProcessInfo():
    nvmlInit()
    handle = nvmlDeviceGetHandleByIndex(0)
    runningProc = nvmlDeviceGetComputeRunningProcesses(handle)
    graphicProc = nvmlDeviceGetGraphicsRunningProcesses(handle)
    process = []
    for i in graphicProc:
        proc = {}
        pid = i.pid
        p = psutil.Process(pid)
        proc['name'] = p.name()
        proc['pid'] = pid
        proc['username'] = p.username()
        used = i.usedGpuMemory / 1048576
        proc['GPUUsage'] = used
        process.append(proc)
    print(process)
    return process
    nvmlShutdown()


if __name__ == "__main__":
    get_gpu_info()
    getProcessInfo()

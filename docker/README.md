# Run docker container

## Using RAPL plugin

The RAPL plugin reads system files and need some specific permissions:

### Perfmon usage

You will need to set the kernel parameter perf_event_paranoid to 0:
Run `sudo sysctl -w kernel.perf_event_paranoid=0` in host before starting the Alumet container.
Note that this command make this parameter temporary and it will be reset after reboot.
If you want to make it persistent check the code of sysctl.

While running the container, you also need to add some capabilities, you can do it through `--cap-add=perfmon --cap-add=sys_nice` flags.

### /sys/devices/virtual/powercap/intel-rapl

In RAPL plugin `/sys/devices/virtual/powercap/intel-rapl` can mounted for two different use cases.
It's not mandatory unless you want to use powercap instead of perfmon. Here are more details:

#### 1/ Powercap usage
In case **perfmon** is disable the plugin will try to use **powercap** and need that dir mounted.
In this case you may need to use **root** user and add capabilities (see --cap-add above) to be able to make powercap works properly.

#### 2/ Consistency check
The RAPL plugin has a **consistency** check that help detect bad behaviors between perf_event and powercap on domain detection.
This check help user by printing warnings in case there are different domains detected by perf_event and powercap. **It's purely informative and doesn't impact measurement** .
For this check to work you need /sys/devices/virtual/powercap/intel-rapl to be mounted, which is masked by default by docker container.

You can overpass it by passing `--security-opt="systempaths=unconfined"` or by using `--privileged` flag (not recommended) or using **root** user (not recommended as well).

In case you're using **podman**, you can also use `--security-opt unmask=/sys/devices/virtual/powercap/intel-rapl` which will only unmask this interface.

Here are the kind of errors logged when consistency check try to start:
```
[2025-03-13T14:09:02Z ERROR plugin_rapl] Cannot read the list of RAPL domains available via the powercap interface: Could not explore /sys/devices/virtual/powercap/intel-rapl. Try to adjust file permissions.

    Caused by:
        No such file or directory (os error 2).
[2025-03-13T14:09:02Z WARN  plugin_rapl] The consistency of the RAPL domains reported by the different interfaces of the Linux kernel cannot be checked (this is useful to work around bugs in some kernel versions on some machines).
```
It doesn't block the execution of RAPL plugin.

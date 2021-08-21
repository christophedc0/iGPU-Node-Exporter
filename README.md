# iGPU-Node-Exporter
A Python based node exporting Intel iGPU data for Prometheus

This has been made & tested for a Intel Xeon E3-1275v6 CPU.


## Requirements
### Apt packages
 - python3
 - python3-pip
 - intel_gpu_tools

### Pip packages
 - prometheus_client
 - subprocess

## Usage
### iGPU host
`python3 script.py port http_service_metric_point`
Real use case: `python3 igpu_exporter.py 9101 http://localhost:9101/metrics`

1. Try the script with the example above
2. Add the service file to `/etc/systemd/system/`
3. Test the service with `systemctl daemon-reload && systemctl start igpu_exporter.service`
4. Check the status with `systemctl status igpu_exporter.py`
5. Add the service to run at boot wiith `systemctl enable igpu_exporter.py`

### Prometheus configuration
Please see `prometheus.yml`

## Required changes for you
 - Adapt path to script in `igpu_exporter.service`
 - Adapt http_service_metric_point in `igpu_exporter.service`

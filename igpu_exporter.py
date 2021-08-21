# Usage example: python3 igpu_exporter.py 9101 http://localhost:9101/metrics

from prometheus_client import start_http_server, Metric, REGISTRY
import sys
import time
import subprocess

class DataCollector(object):
    def __init__(self, endpoint):
        self._endpoint = endpoint
    def collect(self):
        # Fetch the data
        cmd = "/usr/bin/timeout -k 3 3 /usr/bin/intel_gpu_top -J"
        igpu = subprocess.run(cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.PIPE).stdout.decode('utf-8')
        metric = Metric('igpu_video_busy',
            ' Video busy utilisation in %', 'summary')
        metric.add_sample('igpu_video_busy',
            value = igpu.split('engines')[3].split('"Video/0": {\n\t\t\t"busy": ')[1].split(',')[0], labels={})
        yield metric

        metric = Metric('igpu_render_busy',
            'Render busy utilisation in %', 'summary')
        metric.add_sample('igpu_render_busy',
            value = igpu.split('engines')[3].split('"Render/3D/0": {\n\t\t\t"busy": ')[1].split(',')[0], labels={})
        yield metric

        metric = Metric('igpu_enhance_busy',
            'Enhance busy utilisation in %', 'summary')
        metric.add_sample('igpu_enhance_busy',
            value = igpu.split('engines')[3].split('"VideoEnhance/0": {\n\t\t\t"busy": ')[1].split(',')[0], labels={})
        yield metric

        metric = Metric('igpu_power',
            'Power utilisation in W', 'summary')
        metric.add_sample('igpu_power',
            value = igpu.split('"power": {\n\t\t"value": ')[2].split(',')[0], labels={})
        yield metric

if __name__ == '__main__':
    start_http_server(int(sys.argv[1]))
    REGISTRY.register(DataCollector(sys.argv[2]))

    while True: time.sleep(1)

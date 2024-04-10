title: Kubernetes Rightsizing | Cloud Cost Handbook

Without proper resource allocation, Kubernetes clusters can become overprovisioned, leading to wasted resources and increased costs. _Kubernetes rightsizing_ is the process of optimizing resource allocation to find a balance between performance, efficiency, and cost-effectiveness. The goal of rightsizing is to match the resources allocated to each workload with the actual resource requirements of the workload, therefore avoiding overprovisioning.

## Kubernetes Resource Management

Kubernetes [resource management](https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/) is based on setting resource parameters, like CPU (compute) and memory. Kubernetes orchestrates the allocation of pods onto nodes, based on resource requirements, to ensure efficient utilization of cluster resources. Each container within a Kubernetes pod needs a certain amount of CPU and memory to optimally function. Kubernetes provides mechanisms for specifying resource _requests_ and _limits_ for each container in a pod.

- **Resource requests:** The amount of CPU and memory that a container needs to run. A container running within a pod on a node can use more resources than what is specified in its `requests`.
- **Resource limits:** The maximum amount of CPU and memory that a container can consume. Containers cannot use more resources than what’s specified in its `limits`.

The `requests` and `limits` are set within the resources for each container within a pod as follows.

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: demo-pod
spec:
  containers:
    - name: demo-container
      image: demo-image
      resources:
        requests:
          memory: "256Mi"
          cpu: "100m"
        limits:
          memory: "512Mi"
          cpu: "200m"
... 
```

## The Importance of Rightsizing

Rightsizing Kubernetes resources is especially important from both a cost and infrastructure perspective.

- **Cost optimization:** Overprovisioned workloads lead to unnecessary expenses since more resources are allocated than what's required.
- **Performance optimization:** Applications need to have the necessary computing power and memory to perform efficiently. It’s important to properly allocate resources and avoid issues with your applications’ performance. Containers that try to use more resources than allocated, like memory, could run into errors, like `OOMKilled`.
- **Scalability:** During peak usage periods or times (e.g., increased demand based on seasonality), and when you need resources to scale, resources need to be rightsized to meet changing or increased demands. Understanding these peak usage periods better helps to determine how you should rightsize for the future.

## Kubernetes Rightsizing Process

Kubernetes rightsizing is a continuous process to monitor your infrastructure, collect metrics, adjust resources, and finally, review and reassess. The process repeats itself as you continually monitor changes or spikes in usage.

![The Kubernetes rightsizing process with four boxes pointing to each other: Monitor Infrastructure, Collect Metrics, Adjust Resources, Review and Reassess. The last box has an arrow that points back to the first.](/img/kubernetes/rightsize-k8s.png)

- **Monitor Infrastructure:** You can use Kubernetes monitoring tools, like [Prometheus](https://prometheus.io/), to gather insights about resource usage patterns. You can also use other tools, like the [Vantage Kubernetes agent](https://docs.vantage.sh/kubernetes_agent) integration and [rightsizing recommendations](https://docs.vantage.sh/cost_recommendations#kubernetes-rightsizing), to keep an eye on your costs and resource usage over time.
- **Collect Metrics:** Review metrics, like average or maximum usage, for each container. Be sure to review current and historical workload data to make decisions on resource allocation. Rightsizing recommendations in Vantage provide a view of your current configuration, average, and maximum usage for CPU and memory. The chart includes a per-day average usage. The table provides a 30-day average and 30-day average max usage. An estimate of potential monthly savings is also provided based on the recommended configuration.
- **Adjust Resources:** There are several tools and methods you can use to adjust Kubernetes resources. You can manually adjust resources or consider automated alternatives. Some suggestions are provided below.
    - **Horizontal Pod Autoscaler (HPA):** This [Kubernetes tool](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/) automatically scales workloads based on demands. Horizontal scaling indicates that more pods will be deployed. As each load decreases, the HPA will also scale down the pods within the workload.
    - **Vertical Pod Autoscaler (VPA):** You can also vertically scale workloads using the VPA. Vertical scaling means you adjust the existing infrastructure to meet demands rather than adding new pods. [This project](https://github.com/kubernetes/autoscaler/tree/9f87b78df0f1d6e142234bb32e8acbd71295585a/vertical-pod-autoscaler) automatically sets requests for containers based on usage.
    - **Karpenter**: [Karpenter](https://karpenter.sh/) is an open-source autoscaler that was designed for AWS but can also be used with other cloud providers. If pods become unschedulable, Karpenter will provision new nodes. It analyzes any pod requirements and provisions nodes to meet those requirements, as well as removes unneeded nodes. Karpenter consistently watches for underutilized nodes to help decrease cluster compute costs.   
    - **Quality of Service (QOS):** Adjust resource requests and limits to ensure your workloads are assigned the necessary [QOS class](https://kubernetes.io/docs/tasks/configure-pod-container/quality-service-pod/). This ensures your workloads receive the necessary resources when node resources are exceeded.
- **Review and Reassess:** Implement the above measures and continue to review your infrastructure. Repeat this analysis and respond to changes over time.

## Kubernetes Rightsizing Example

In the following example, a Kubernetes Deployment for a web app consists of a single container running a Node.js server. The initial resource `requests` and `limits` for this container are set as follows.

```yaml
...
spec:
  containers:
    - name: nodejs-dev-server
      image: test-nodejs-image
      resources:
        requests:
          memory: "1000Mi"
          cpu: "1000m"
        limits:
          memory: "2000Mi"
          cpu: "2000m"
...
```

Based on the above configuration:

- The container’s `requests` parameter is set to 1000 MiB of memory and 1000 mCPU to run.
- The container’s `limits` parameter is set to 2000 MiB of memory and 2000 mCPU.

Over time, the actual resource utilization is _significantly lower_ than the currently allocated resources. The application, on average, uses about 300 MiB of memory and 200 mCPU under normal operating conditions. In this case, the workload is overprovisioned. The allocated resources exceed the actual requirements of the application, which could lead to higher costs and wasted resources.

In the example below, this container is monitored by the Vantage Kubernetes agent and rightsizing recommendations. Average and maximum usage are provided along with the recommended suggestion to rightsize and potential monthly savings.

![The Kubernetes Rightsizing UI in the Vantage console with a sample recommendation](/img/kubernetes/k8s-rightsizing-ui.png)

To address this overprovisioning, you can rightsize the workload by adjusting the resource `requests` based on the observed resource utilization. Rightsizing recommendations in Vantage aim for an efficiency target of 80%. This ensures more efficient resource utilization and cost optimization within the Kubernetes cluster and that resources have a reasonable buffer to handle small spikes in usage.

You also set `limits` equal to `requests`, which corresponds with a [QOS class](https://kubernetes.io/docs/concepts/workloads/pods/pod-qos/#guaranteed) of `Guaranteed`. Per Kubernetes, the `Guaranteed` QOS class has the "strictest resource limits and [is] least likely to face eviction." You adjust your resources as follows.

```yaml
...
spec:
	containers:
	- name: nodejs-server
	  image: test-nodejs-image
	  resources:
	    requests:
	      memory: "375Mi"
	      cpu: "250m"
	    limits:
	      memory: "375Mi"
	      cpu: "250m"
...
```

With these recommendations in place, you can continue to monitor your usage and adjust accordingly.

!!! Contribute
    Contribute to this page on [GitHub](https://github.com/vantage-sh/handbook) or join the `#cloud-costs-handbook` channel in the [Vantage Community Slack](https://vantage.sh/slack).

_Last updated Apr 9, 2024_

import json
import boto3

service_list = []

ssmClient = boto3.client("ssm", region_name = "us-east-1")

list_service_path = ssmClient.get_parameters_by_path(
    Path = "/aws/service/global-infrastructure/services"
)
if len(list_service_path["Parameters"]) > 0:
    for pathData in list_service_path["Parameters"]:
        list_service_names = ssmClient.get_parameters_by_path(
            Path = pathData["Name"]
        )
        service_list.append(list_service_names["Parameters"][0]["Value"])

if "NextToken" in list_service_path:
    NextToken = list_service_path["NextToken"]
    while True:
        list_service_path = ssmClient.get_parameters_by_path(
            Path = "/aws/service/global-infrastructure/services",
            NextToken = NextToken
        )
        if len(list_service_path["Parameters"]) > 0:
            for pathData in list_service_path["Parameters"]:
                list_service_names = ssmClient.get_parameters_by_path(
                    Path = pathData["Name"]
                )
                service_list.append(list_service_names["Parameters"][0]["Value"])
        
        if "NextToken" in list_service_path:
            NextToken = list_service_path["NextToken"]
        else:
            break

print(len(service_list))
service_list.sort(key=lambda x:(not x.islower(), x))
[print('| {} | {} |'.format(i, s)) for i, s in enumerate(service_list)]
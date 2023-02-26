from diagrams import Cluster, Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.network import ELB
from diagrams.aws.network import NATGateway
from diagrams.aws.network import PublicSubnet, PrivateSubnet
from diagrams.aws.network import RouteTable
from diagrams.aws.network import VPC, InternetGateway

with Diagram("VPC with subnets", show=False):
    with Cluster("VPC"):
        vpc = VPC("VPC\n10.0.0.0/16")
        igw = InternetGateway("IGW")

        with Cluster("Public Subnets"):
            pub_sub1 = PublicSubnet("Public\n10.0.1.0/24")
            pub_sub2 = PublicSubnet("Public\n10.0.2.0/24")
            pub_rt = RouteTable("Public RT")
            pub_rt >> pub_sub1 >> EC2("Public EC2")
            pub_rt >> pub_sub2 >> EC2("Public EC2")
            igw >> pub_rt

        with Cluster("Private Subnets"):
            pri_sub1 = PrivateSubnet("Private\n10.0.3.0/24")
            pri_sub2 = PrivateSubnet("Private\n10.0.4.0/24")
            pri_rt = RouteTable("Private RT")
            pri_rt >> pri_sub1 >> NATGateway("NAT Gateway")
            pri_rt >> pri_sub2 >> NATGateway("NAT Gateway")

        vpc >> igw
        vpc >> pub_sub1
        vpc >> pub_sub2
        vpc >> pri_sub1
        vpc >> pri_sub2
        vpc >> pub_rt
        vpc >> pri_rt

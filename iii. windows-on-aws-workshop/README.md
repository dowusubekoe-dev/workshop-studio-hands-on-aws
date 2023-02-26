# Windows on AWS Workshop

## Introduction
This workshop will teach you about the basic concepts for running Windows Workloads on AWS. In this workshop you will get hands on with Windows Server 2019 hosted on EC2, Managed Microsoft AD running on AWS Directory Services and hosting a Windows File Server on Amazon FSx. This will teach you the basics of running Windows on AWS and allow you to take your knowledge and go build Production ready systems on Amazon Web Services.

## Setup network using VPC and AWS CloudFormation
We will launch a CloudFormation template that will define the following resources for an Amazon Virtual Private Cloud (VPC):

- A VPC with a CIDR block of 10.0.0.0/16.
- Two public subnets and two private subnets launched across two Availability zones, each containing 250 available IPv4 addresses.
- Route Tables corresponding to each subnet, allowing us to define internet routes and isolated routes in and out of our VPC.
- An internet Gateway (IGW) that enables communication between the VPC and the internet.
- Two Network Address Translation (NAT) Gateways that will allow Amazon EC2 instances housed within the private subnets to connect to services outside of the VPC but prevents such external services or the internet from initiating a connection with those instances.
- Two Security Groups that will control network access in and out of our Amazon EC2 instances.

VPC Endpoints for AWS Systems Manager. This enables a connection between the VPC and the AWS Systems Manager services without traffic to/from those services traversing the public internet. Systems Manager will be explained later on in the course.

## Create and deploy AWS Managed Microsoft Active Directory

## Deploy a Windows File Server using Amazon FSx for Windows File Server

## Administering Active Directory and Windows File Server using Amazon EC2
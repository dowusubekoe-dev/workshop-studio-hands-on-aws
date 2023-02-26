# Basic Modules
This module will introduce you to understanding of the various functions of each AWS foundational service.
**Basic modules consist of the following services**:
- Compute - Amazon EC2
- Network - Amazon VPC
- Security - AWS IAM
- Monitoring - Amazon CloudWatch
- Database - Amazon RDS
- Storage - Amazon S3, Amazon Elastic File System

## Compute - Amazon EC2
To start and operate your organization, computing is the essential first step, regardless of whether you're creating enterprise, cloud-native, or mobile applications, or managing large clusters for data analysis. AWS provides a broad range of computing services that enable you to build, deploy, manage, and expand your applications and workloads in the world's most potent, reliable, and inventive computing cloud.
**The computing services offered by AWS possess the following traits**:
- Apt computing services for your specific workloads
- Speedy transition from idea to market
- Integrated security features
- Adaptability for cost optimization
- Availability of computing resources in your desired location

### Amazon EC2 Overview
**Amazon Elastic Compute Cloud (EC2)** is a web service that provides resizable compute capacity in the cloud. It allows users to launch and manage virtual servers, called instances, on Amazon's infrastructure, making it easy to scale capacity up or down as needed. EC2 instances can be used for a wide variety of computing tasks, from running simple web applications to complex big data processing jobs.

<center>

![Amazon EC2 Overview](/docs/assets/amazon-ec2-architecture.svg)

</center>

#### Steps to complete the lab
The lab will be completed using the following steps
- **Create a new key pair**
    - Navigate to https://us-east-1.console.aws.amazon.com/ec2/home?region=us-east-1#KeyPairs:
    - Click "Create key pair"

    <center>

    ![Click on Create Key Pair](/docs/assets/create-new-key-pair.jpeg)

     </center>

    - Type "demoWindowKeyPair"

     <center>

    ![Click on Create Key Pair](/docs/assets/add-the-name-field.jpeg)

     </center>

    - Click "Create key pair"

     <center>

    ![Click on Create Key Pair](/docs/assets/create-key-pairs.jpeg)

     </center>
     
- **Launch a Web Server Instance**
    - Navigate to https://us-east-1.console.aws.amazon.com/ec2/home?region=us-east-1#LaunchInstances:
    - Click the "Name" field. Type "demoWebServer-IMD"

    <center>

    ![enter-instance-name](/docs/assets/enter-name-filed.jpeg)

    </center>

    - Browse for AMI type
     <center>

     ![browse-ami](/docs/assets/browse-ami.jpeg)

    </center>

    - Click dropdown and select the Key Pair "demoWindowKeyPair"

     <center>

     ![select-key-pair](/docs/assets/create-key-pairs.jpeg)

    </center>

    - Select VPC, Subnet and Enable "Auto-assign public IP"

     <center>

     ![select-vpc-subnet](/docs/assets/vpc-subnet-auto_ip.jpeg)

    </center>

     <center>

     ![enter-instance-name](/docs/assets/enter-name-filed.jpeg)

    </center>

     <center>

     ![enter-instance-name](/docs/assets/enter-name-filed.jpeg)

    </center>

     <center>

     ![enter-instance-name](/docs/assets/enter-name-filed.jpeg)

    </center>

     <center>

     ![enter-instance-name](/docs/assets/enter-name-filed.jpeg)

    </center>

- Connect to your linux instance
- Connect to your Linux instance using Session Manager (Optional)
- Connect to EC2 Instance using PuTTy (Optional)
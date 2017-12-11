# Turn into a pumpkin

This is a short script for AWS to downsize a box after a heavy job has finished.

## Example usage

To turn into a pumpkin after a long job:

    ./long_job.sh && pumpkin2

To turn into a big pumpkin immediately:

    pumpkin2 m4.10xlarge

## The problem

  I used to have to manually resize my development EC2 box, which is a comically tedious process:

1. Go to AWS console
2. Type in password
3. Take out phone, type in 2FA
4. Open EC2 instances tab
5. Find my node in the list
6. Shut it down
7. Wait for it to shut down
8. Right click and change the type
9. Restart the box
10. Wait for it to boot

  Instead, I wanted a script that could do all this for me.

## Implementation

  Amazon provides a CLI tool for most of the services, which is capable of resizing a box; however,
it is not able to resize a box that is running; you can't resize yourself.

  To work around this, you can instead create a lambda function, which can shut down the dev box, resize
and restart it.

## Setup

1. Create a AWS lambda function using `lambda_pumpkin.py` - it will need EC2 permissions.
2. Copy `pumpkin2` to your box, and run it as needed.

Old `pumpkin` is still here for historical reasons, but you probably don't want to use it.


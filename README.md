# dude_wheres_my_bench

To set up:
Need a Raspberry Pi with the camera attachment.

Source the following statements with your API Keys
```
# Twillio
export tw_acc_api="key"
export tw_auth_token="key"
export number="number"
```

Configure awscli for python with your secret / public keys. Im sure you can source these too if you want
```
aws configure
```

take_pictures.py is the main file that handles logic and whatnot. Run that and it should be golden.

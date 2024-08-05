# Whatsapp messages

The mode is pretty straight forward to use.

You will need:
- phone number or group id
- message

All the other options can be obtain automatically.

The script use 2 funtions:
- sendwhatmsg_instantly --> to send a message to a specific person
- sendwhatmsg_to_group_instantly --> to send a message to an specific group

```
(function) def sendwhatmsg_instantly(
    phone_no: str,
    message: str,
    wait_time: int = 15,
    tab_close: bool = False,
    close_time: int = 3
) -> None
```

```
(function) def sendwhatmsg_to_group_instantly(
    group_id: str,
    message: str,
    wait_time: int = 15,
    tab_close: bool = False,
    close_time: int = 3
) -> None
```

Based on: https://morioh.com/a/7fca330c3b74/send-whatsapp-messages-using-python
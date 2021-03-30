program lbpcom16;

{$IFDEF WINDOWS}
uses synaser,synautil,synaip,blcksock,dos,crt;
var
ser:TBlockSerial;
TheComPort : string;
IPAddr : string;
Socket : TUDPBlockSocket;
{$ELSE}
uses dos,crt;
var TheComPort : word;
{$ENDIF}


{$I SELECTC}
{$I SELECTIO}
{I SELECTP}
{$I SELECTPR}
{$I INTERFCE}
var

Byte0 : byte;
Byte1 : byte;
Byte2 : byte;
Byte3 : byte;

Word0 : word;

Word1 : word;

procedure Usage;
begin
  writeln('Usage: setipaddr xx xx xx xx');
  writeln;
  halt(2);
end;



procedure Error(err : integer);
begin
  writeln(errorrecord[err].errstr);
  halt(2);
end;


procedure GetParms;
var
retcode : integer;
begin
  if ParamCount < 4 then Usage;
  val(ParamStr(1),Byte3,retcode);
  if retcode <> 0 then BumOut('Bad IP address octet 3');
  val(ParamStr(2),Byte2,retcode);
  if retcode <> 0 then BumOut('Bad IP address octet 2');
  val(ParamStr(3),Byte1,retcode);
  if retcode <> 0 then BumOut('Bad IP address octet 1');
  val(ParamStr(4),Byte0,retcode);
  if retcode <> 0 then BumOut('Bad IP address octet 0');

end;

begin
  GetOurEnv;
  if not InitializeInterface(message) then bumout(message);
  GetParms;
  write('Old Address: ');
  Word0 := ELBP16ReadEEEP($0020);
  Word1 := ELBP16ReadEEEP($0022);
  write((Word1 SHR 8),':',(Word1 and 255),':');
  write((Word0 SHR 8),':',(Word0 and 255),':');
  writeln;
  ELBP16WriteEEEP($0020,Byte0+(Byte1 SHL 8));
  ELBP16WriteEEEP($0022,Byte2+(Byte3 SHL 8));
  write('New Address: ');
  Word0 := ELBP16ReadEEEP($0020);
  Word1 := ELBP16ReadEEEP($0022);
  write((Word1 SHR 8),':',(Word1 and 255),':');
  write((Word0 SHR 8),':',(Word0 and 255),':');
  writeln;

end.
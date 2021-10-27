
Lecture 11　MySQL資料庫權限管理

--------------------------------------------------------------------------------

11-1　帳號與密碼

> create user lynn.915@localhost;
> create user lynn.916@localhost identified by "samuel0916";　#設定登入密碼
> select host, user, password from [mysql.]user;　#紀錄於系統資料庫mysql，密碼經加密處理

> set password=password("samuel0915");　#password: 密碼函數
> set password for lynn.915=password("samuel0915");
> drop user lynn.915@localhost;　#set, drop指令對系統設定
> update mysql.user set password=password("samuel0915")
  where user=user()/lynn.916;
  flush privileges;
> delete from mysql.user where user="lynn.915";　#update, delete針對user資料表直接修改
  flush privileges;　#修改資料表時，需同步更新權限狀態


--------------------------------------------------------------------------------

11-2　帳號授權

1.權限授權
 > grant/revoke all on *.*;　#全域授權: 紀錄於mysql.users
 > grant/revoke all on database.*;　#資料庫授權: 紀錄於mysql.db
 > grant/revoke all on database.table;　#資料表授權: 紀錄於mysql.tables_priv
 > grant/revoke all on database.table(column);　#欄位授權: 紀錄於mysql.columns_priv


2.結合使用者帳號
 > grant all on *.* to lynn.915@"%" identified by "samuel0915";　#全域授權: 全IP登入
 > grant all on db.* to lynn.915@localhost identified by "samuel0915";　#資料庫授權: 本地登入
 > grant all on db.emp to lynn.915@192.168.1.100 identified by "samuel0915";　#資料表授權: 限定IP登入
 > grant select, create, alter, drop on db.* to lynn.915@localhost;　#資料庫授權: DDL權限
 > grant select, insert, update, delete on db.emp to lynn.915@localhost;　#資料表授權: DML權限
   [with grant option;]　#再授權的權力


--------------------------------------------------------------------------------

11-3　遠端連線

> mysql --user=(帳號) --password=(密碼) --host=(IP位址) --port=(連接埠)
> mysql -u (帳號) -p(密碼) -h (IP位址) -P (連接埠)　#password無空白間隔，port為P大寫

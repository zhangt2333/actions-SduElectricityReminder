<div align="center">
<h1 align="center">SDU 青岛校区电量自动查询，低电提醒</h1>
</div>


## 简介

每天定时自动查询 [青岛校区] 宿舍电量，低电量提醒！！！
* 不需要自己购买服务器，也不需要自己配置服务器，Serverless !!
* 如想修改定时运行的时间，可修改 `.github/workflows/SduElectricityReminder.yml` 中 `schedule` 属性。


## Github Actions 启用步骤

### 1. Fork 本项目

Fork 本项目: [zhangt2333/actions-SduElectricityReminder](https://github.com/zhangt2333/actions-SduElectricityReminder) (Star 自然是更好)

### 2. 准备需要的 Secrets 参数

1. `CLI_OPTS`: VPN 账号密码配置
    * 查询电量的服务器在校园网内网，通过 VPN 连入校园网需要 VPN 账号，即 SDU 学号和统一认证密码，随后会写入 Github 仓库的 Secrets 中

```
-d https://vpn.sdu.edu.cn -u VPN账号 -p VPN密码
```

2. `DATA`: 宿舍楼配置

    * `account`: 6位校园卡账户
    * `building`: 宿舍楼, 只能从 ['T1', 'T3', 'S1一多书院', 'S2从文书院', 'S5凤凰居5号楼', 'S6凤凰居6号楼', '凤凰居6号楼', 'S7凤凰居7号楼', 'S8凤凰居8号楼', 'S9凤凰居9号楼', '凤凰居9号楼', 'S10凤凰居10号楼', 'S11'] 中选一个
    * `room`: 宿舍号，一般是 A/B + 3位数字的格式
    * `threshold`: 电量低于多少会报警
```
{
    'account': '000000',
    'building': 'S2从文书院',
    'room': 'B666',
    'threshold': 100.00
}
```

### 3. 启用 Github Actions

![](README/img1.png)

### 4. 将参数填到 Secrets

将填好的参数加入到 Secrets 中，name 为 `DATA`，value 为步骤 2 中的多行字符串

![](README/img2.png)

![](README/img3.png)

![](README/img4.png)

### 5. 配置自己账号的邮件提醒
* 如下图正确配置，这样运行失败（电量过低）的 Github Actions 事件会自动邮件通知你
![](README/img5.png)

## Credits

* https://github.com/Yuandiaodiaodiao/sdu-electric-charge 提供的电量查询爬虫
* https://github.com/Hagb/docker-easyconnect 提供 docker 封装 easyconnect
* https://github.com/zhangt2333/SDU-Funny-Scripts 有很多有关 SDU 校园生活的爬虫/脚本
* https://github.com/zhangt2333/actions-easyconnect 提供在 easyconnect 中运行代码的 Github Actions

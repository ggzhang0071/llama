sql_query = '''根据给出的表结构，以下是生成的20个指标和对应的SQL查询：

指标1： 总记录数

sql
Copy code
SELECT COUNT(*) AS total_records FROM mj_auth_role;
指标2： 不同角色类型的数量

sql
Copy code
SELECT type, COUNT(*) AS type_count FROM mj_auth_role GROUP BY type;
指标3： 不同角色类型的角色名称列表

sql
Copy code
SELECT type, GROUP_CONCAT(name) AS role_names FROM mj_auth_role GROUP BY type;
指标4： 不同角色类型的平均角色编码字符长度

sql
Copy code
SELECT type, AVG(LENGTH(code)) AS avg_code_length FROM mj_auth_role GROUP BY type;
指标5： 不同角色类型的最早创建时间和最晚修改时间

sql
Copy code
SELECT type, MIN(gmt_create) AS earliest_create_time, MAX(gmt_modified) AS latest_modify_time FROM mj_auth_role GROUP BY type;
指标6： 不同角色类型的角色数量和平均角色编码字符长度

sql
Copy code
SELECT type, COUNT(*) AS role_count, AVG(LENGTH(code)) AS avg_code_length FROM mj_auth_role GROUP BY type;
指标7： 不同角色类型的内置角色数量

sql
Copy code
SELECT type, SUM(CASE WHEN is_built = 0 THEN 1 ELSE 0 END) AS built_in_role_count FROM mj_auth_role GROUP BY type;
指标8： 不同角色类型的角色数量和内置角色数量

sql
Copy code
SELECT type, COUNT(*) AS role_count, SUM(CASE WHEN is_built = 0 THEN 1 ELSE 0 END) AS built_in_role_count FROM mj_auth_role GROUP BY type;
指标9： 不同角色类型的平均软删标志值

sql
Copy code
SELECT type, AVG(is_del) AS avg_is_del FROM mj_auth_role GROUP BY type;
指标10： 不同角色类型的角色数量和平均软删标志值

sql
Copy code
SELECT type, COUNT(*) AS role_count, AVG(is_del) AS avg_is_del FROM mj_auth_role GROUP BY type;
指标11： 不同角色类型的角色数量和平均角色类型

sql
Copy code
SELECT type, COUNT(*) AS role_count, AVG(type) AS avg_type FROM mj_auth_role GROUP BY type;
指标12： 不同角色类型的角色数量和平均创建用户ID

sql
Copy code
SELECT type, COUNT(*) AS role_count, AVG(creator_id) AS avg_creator_id FROM mj_auth_role GROUP BY type;
指标13： 不同角色类型的角色数量和平均修改用户ID

sql
Copy code
SELECT type, COUNT(*) AS role_count, AVG(modifier_id) AS avg_modifier_id FROM mj_auth_role GROUP BY type;
指标14： 不同角色类型的角色数量和角色名称列表

sql
Copy code
SELECT type, COUNT(*) AS role_count, GROUP_CONCAT(name) AS role_names FROM mj_auth_role GROUP BY type;
指标15： 不同角色类型的平均角色描述字符长度

sql
Copy code
SELECT type, AVG(LENGTH(remark)) AS avg_remark_length FROM mj_auth_role GROUP BY type;
指标16： 不同角色类型的角色数量和平均角色描述字符长度

sql
Copy code
SELECT type, COUNT(*) AS role_count, AVG(LENGTH(remark)) AS avg_remark_length FROM mj_auth_role GROUP BY type;
指标17： 不同角色类型的角色数量和角色编码列表

sql
Copy code
SELECT type, COUNT(*) AS role_count, GROUP_CONCAT(code) AS role_codes FROM mj_auth_role GROUP BY type;
指标18： 不同角色类型的平均角色名称字符长度

sql
Copy code
SELECT type, AVG(LENGTH(name)) AS avg_name_length FROM mj_auth_role GROUP BY type;
指标19： 不同角色类型的角色数量和平均角色名称字符长度

sql
Copy code
SELECT type, COUNT(*) AS role_count, AVG(LENGTH(name)) AS avg_name_length FROM mj_auth_role GROUP BY type;
指标20： 不同角色类型的平均角色类型和平均软删标志值

sql
Copy code
SELECT type, AVG(type) AS avg_type, AVG(is_del) AS avg_is_del FROM mj_auth_role GROUP BY type;
请注意，上述SQL查询仅为示例，实际应用时可能需要根据具体情况进行修改。数据表的字段名和数据类型也需要根据实际情况进行调整。
'''



-- 0. my privileges
SELECT user, host, db, table_name, privilege_type
FROM information_schema.role_table_grants
WHERE grantee = "'user_0d_1'@'localhost'" OR grantee = "'user_0d_2'@'localhost';

def parent_sql_query(n):
    sql_query = '''
                    SELECT 
                        id,
                        name,
                        email,
                        created_at,
                        updated_at,
                        count as children_count
                    FROM
                    (
                        (
                            SELECT * FROM
                                (
                                    SELECT parent_id, COUNT(parent_id)
                                    FROM association 
                                    GROUP BY parent_id
                                ) as table_1
                            WHERE count = {}
                        ) table_2

                        LEFT JOIN

                        (SELECT * FROM "Parent") table_3

                        ON table_2.parent_id = table_3.id

                    ) table_4
                '''.format(n)
    return sql_query

def child_sql_query(n):
    sql_query = '''
                    SELECT 
                        id,
                        name,
                        email,
                        created_at,
                        updated_at,
                        count as parents_count
                    FROM
                    (
                        (
                            SELECT * FROM
                                (
                                    SELECT child_id, COUNT(child_id)
                                    FROM association 
                                    GROUP BY child_id
                                ) as table_1
                            WHERE count = {}
                        ) table_2

                        LEFT JOIN

                        (SELECT * FROM "Child") table_3

                        ON table_2.child_id = table_3.id

                    ) table_4
                '''.format(n)
    return sql_query

from connect_db import Database


def create_tables():

    staff_category_table = """
        CREATE TABLE staff_category(
            staff_category_id SERIAL PRIMARY KEY,
            name VARCHAR(25),
            last_update DATE DEFAULT now(),
            create_date TIMESTAMP DEFAULT now());
    """

    staff_table = """
        CREATE TABLE staff(
            staff_id SERIAL PRIMARY KEY,
            first_name VARCHAR(25),
            last_name VARCHAR(25),
            staff_category_id INT REFERENCES staff_category(staff_category_id),
            last_update DATE DEFAULT now(),
            create_date TIMESTAMP DEFAULT now());
    """

    product_table = """
        CREATE TABLE product(
            product_id SERIAL PRIMARY KEY,
            name VARCHAR(25),
            create_date TIMESTAMP DEFAULT now());
    """

    expired_product_table = """
        CREATE TABLE expired_product(
            expired_product_id SERIAL PRIMARY KEY,
            name VARCHAR(25),
            create_date TIMESTAMP DEFAULT now());
    """

    storehouse_table = """
        CREATE TABLE storehouse(
            storehouse_id SERIAL PRIMARY KEY,
            name VARCHAR(25),
            product_id INT REFERENCES product(product_id),
            expired_product_id INT REFERENCES expired_product(expired_product_id),
            staff_category_id INT REFERENCES staff_category(staff_category_id),
            create_date TIMESTAMP DEFAULT now());
    """

    payment_table = """
        CREATE TABLE payment(
            payment_id SERIAL PRIMARY KEY,
            cash NUMERIC,
            card NUMERIC,
            last_up DATETIME DEFAULT now(),
            create_date TIMESTAMP DEFAULT now());
    """

    consumer_table = """
        CREATE TABLE consumer(
            consumer_id SERIAL PRIMARY KEY,
            product_id INT REFERENCES product(product_id),
            payment_id INT REFERENCES payment(payment_id),
            branch_id INT REFERENCES branch(branch_id),
            create_date TIMESTAMP DEFAULT now());
    """

    branch_table = """
        CREATE TABLE branch(
            branch_id SERIAL PRIMARY KEY,
            name VARCHAR(25),
            staff_category_id INT REFERENCES staff_category(staff_category_id),
            create_date TIMESTAMP DEFAULT now());
    """

    city_table = """
        CREATE TABLE city(
            city_id SERIAL PRIMARY KEY,
            name VARCHAR(25),
            brand_id INT REFERENCES branch(brand_id),
            create_date TIMESTAMP DEFAULT now());
    """

    country_table = """
        CREATE TABLE country(
            country_id SERIAL PRIMARY KEY,
            name VARCHAR(25),
            city_id INT REFERENCES city(city_id),
            create_date TIMESTAMP DEFAULT now());
    """

    data = {
        "staff_category_table" : staff_category_table,
        "staff_table" : staff_table,
        "product_table" : product_table,
        "expired_product_table" : expired_product_table,
        "storehouse_table" : storehouse_table,
        "payment_table" : payment_table,
        "consumer_table" : consumer_table,
        "branch_table" : branch_table,
        "country_table" : country_table,
        "city_table" : city_table,
    }

    for i in data:
        print(f"{i} {Database.connect(data[i], "create")}")


if __name__ == "__main__":
    create_tables()
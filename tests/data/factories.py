from faker import Faker

fake = Faker()


def user_factory(count):
    for _ in range(count):
        yield {
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
        }

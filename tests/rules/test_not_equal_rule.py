import unittest
from faker import Faker
from tests.mocks import mock_product, Product, mock_orders, mock_locale_names
from validationpy.results.validation_state import ValidationState
from validationpy.rules.not_equal_rule import NotEqualRule


class TestNotEqualRule(unittest.TestCase):
    def setUp(self) -> None:
        self.faker = Faker()
        self.product = mock_product(self.faker)

    # region validate
    # region StringTypes
    def test_validate_should_return_true_when_equal_str(self):
        # Arrange
        object_to_validate = self.product
        state = ValidationState(object_to_validate)
        value_to_compare = self.faker.name()
        rule = NotEqualRule[Product, str](value_to_compare)

        # Act & Assert
        self.assertTrue(rule.validate(state, self.product.name))
        self.assertFalse('comparison_value' in state.message_constructor.placeholders.keys())

    def test_validate_should_return_false_when_not_equal_str(self):
        # Arrange
        object_to_validate = self.product
        state = ValidationState(object_to_validate)
        value_to_compare = self.product.name
        rule = NotEqualRule[Product, str](value_to_compare)

        # Act & Assert
        self.assertFalse(rule.validate(state, self.product.name))
        self.assertEqual(value_to_compare, state.message_constructor.placeholders['comparison_value'])
    # endregion

    # region NumericTypes
    def test_validate_should_return_true_when_equal_int(self):
        # Arrange
        object_to_validate = self.product
        state = ValidationState(object_to_validate)
        value_to_compare = self.faker.pyint(min_value=1)
        rule = NotEqualRule[Product, int](value_to_compare)

        # Act & Assert
        self.assertTrue(rule.validate(state, self.product.identifier))
        self.assertFalse('comparison_value' in state.message_constructor.placeholders.keys())

    def test_validate_should_return_false_when_not_equal_int(self):
        # Arrange
        object_to_validate = self.product
        state = ValidationState(object_to_validate)
        value_to_compare = self.product.identifier
        rule = NotEqualRule[Product, int](value_to_compare)

        # Act & Assert
        self.assertFalse(rule.validate(state, self.product.identifier))
        self.assertEqual(value_to_compare, state.message_constructor.placeholders['comparison_value'])

    def test_validate_should_return_true_when_equal_float(self):
        # Arrange
        object_to_validate = self.product
        state = ValidationState(object_to_validate)
        value_to_compare = self.faker.pyfloat(min_value=0.1)
        rule = NotEqualRule[Product, float](value_to_compare)

        # Act & Assert
        self.assertTrue(rule.validate(state, self.product.quantity_available))
        self.assertFalse('comparison_value' in state.message_constructor.placeholders.keys())

    def test_validate_should_return_false_when_not_equal_float(self):
        # Arrange
        object_to_validate = self.product
        state = ValidationState(object_to_validate)
        value_to_compare = self.product.quantity_available
        rule = NotEqualRule[Product, float](value_to_compare)

        # Act & Assert
        self.assertFalse(rule.validate(state, self.product.quantity_available))
        self.assertEqual(value_to_compare, state.message_constructor.placeholders['comparison_value'])

    def test_validate_should_return_true_when_equal_complex(self):
        # Arrange
        object_to_validate = self.product
        state = ValidationState(object_to_validate)
        value_to_compare = 2+1j
        rule = NotEqualRule[Product, complex](value_to_compare)

        # Act & Assert
        self.assertTrue(rule.validate(state, 1 + 1j))
        self.assertFalse('comparison_value' in state.message_constructor.placeholders.keys())

    def test_validate_should_return_false_when_not_equal_complex(self):
        # Arrange
        object_to_validate = self.product
        state = ValidationState(object_to_validate)
        value_to_compare = 1+1j
        rule = NotEqualRule[Product, complex](value_to_compare)

        # Act & Assert
        self.assertFalse(rule.validate(state, 1 + 1j))
        self.assertEqual(value_to_compare, state.message_constructor.placeholders['comparison_value'])
    # endregion

    # region SequenceTypes
    def test_validate_should_return_true_when_equal_list(self):
        # Arrange
        object_to_validate = self.product
        state = ValidationState(object_to_validate)
        value_to_compare = mock_orders(self.product.identifier, self.faker, 5)
        rule = NotEqualRule[Product, list](value_to_compare)

        # Act & Assert
        self.assertTrue(rule.validate(state, self.product.orders))
        self.assertFalse('comparison_value' in state.message_constructor.placeholders.keys())

    def test_validate_should_return_false_when_not_equal_list(self):
        # Arrange
        object_to_validate = self.product
        state = ValidationState[Product](object_to_validate)
        value_to_compare = self.product.orders
        rule = NotEqualRule[Product, list](value_to_compare)

        # Act & Assert
        self.assertFalse(rule.validate(state, self.product.orders))
        self.assertEqual(value_to_compare, state.message_constructor.placeholders['comparison_value'])

    def test_validate_should_return_true_when_equal_tuple(self):
        # Arrange
        object_to_validate = self.product
        state = ValidationState[Product](object_to_validate)
        value_to_compare = (self.faker.pyfloat(min_value=0.1), self.faker.currency_code())
        rule = NotEqualRule[Product, tuple](value_to_compare)

        # Act & Assert
        self.assertTrue(rule.validate(state, self.product.currency))
        self.assertFalse('comparison_value' in state.message_constructor.placeholders.keys())

    def test_validate_should_return_false_when_not_equal_tuple(self):
        # Arrange
        object_to_validate = self.product
        state = ValidationState[Product](object_to_validate)
        value_to_compare = self.product.currency
        rule = NotEqualRule[Product, tuple](value_to_compare)

        # Act & Assert
        self.assertFalse(rule.validate(state, self.product.currency))
        self.assertEqual(value_to_compare, state.message_constructor.placeholders['comparison_value'])
    # endregion

    # region MappingType
    def test_validate_should_return_true_when_equal_dict(self):
        # Arrange
        object_to_validate = self.product
        state = ValidationState[Product](object_to_validate)
        value_to_compare = mock_locale_names(self.faker, 5)
        rule = NotEqualRule[Product, dict](value_to_compare)

        # Act & Assert
        self.assertTrue(rule.validate(state, self.product.locale_names))
        self.assertFalse('comparison_value' in state.message_constructor.placeholders.keys())

    def test_validate_should_return_false_when_not_equal_dict(self):
        # Arrange
        object_to_validate = self.product
        state = ValidationState[Product](object_to_validate)
        value_to_compare = self.product.locale_names
        rule = NotEqualRule[Product, dict](value_to_compare)

        # Act & Assert
        self.assertFalse(rule.validate(state, self.product.locale_names))
        self.assertEqual(value_to_compare, state.message_constructor.placeholders['comparison_value'])
    # endregion
    # endregion

    # region get_template_message
    def test_get_template_message_should_return_template(self):
        # Arrange
        rule = NotEqualRule[object, object](object)

        # Act
        template = rule.get_template_message()

        # Assert
        self.assertEqual("'$attribute_name' must not be equal to '$comparison_value'",
                         template.template)
    # endregion


if __name__ == '__main__':
    unittest.main()

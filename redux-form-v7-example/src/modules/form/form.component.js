import React from 'react';
import { Field } from 'redux-form';

import Text from '../components/text';
import Select from '../components/select';
import Radio from '../components/radio';
import Checkbox from '../components/checkbox';
import Datepicker from '../components/datepicker';

import { required } from './form.validators'

export const FormComponent = ({ handleSubmit, onSubmit, formValues, change }) => {
  return (
    <div className="flex flex-column justify-center items-center">
      <h1>My Very own Form</h1>
      <form
        className="w-80"
        onSubmit={handleSubmit(onSubmit)}
      >
        <Field
          name="firstName"
          label="First Named"
          component={Text}
          validate={required}
        />
        <Field
          name="lastName"
          label="Last Name"
          component={Text}
        />
        <Field
          name="email"
          label="Email"
          component={Text}
        />
        <Field
          name="meatChoice"
          label="Meat Choice"
          component={Select}
          options={{
            pork: 'Pork',
            beef: 'Beef',
            chicken: 'Chicken'
          }}
        />
        <Field
          name="spiceLevel"
          label="Spice Level"
          component={Radio}
          options={{
            mild: 'Mild',
            medium: 'Medium',
            hot: 'hot'
          }}
        />
        {formValues && formValues.spiceLevel === 'hot' ? (
          <Field
            name="wantsFries"
            label="Would you like fries with that?"
            component={Checkbox}
          />
        ) : ''}
        <Field
          name="orderDate"
          label="Order Date"
          component={Datepicker}
          change={change}
        />

        <button
          type="submit"
          className="link br2 bg-blue white dim pa3 f6 sans-serif b--blue ba"
        >
          Submit
        </button>
      </form>
    </div>
  );
}

export default FormComponent;

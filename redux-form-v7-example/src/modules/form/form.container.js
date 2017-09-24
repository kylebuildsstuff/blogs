import React from 'react';
import { connect } from 'react-redux';
import { reduxForm, getFormValues } from 'redux-form';

import FormComponent from './form.component';

export const FormContainer = props => {
  const submitForm = (formValues) => {
    console.log('submitting Form: ', formValues);
  }

  return (
    <FormComponent
      formValues={props.formValues}
      change={props.change}
      onSubmit={submitForm}
      handleSubmit={props.handleSubmit}
    />
  );
}

const mapStateToProps = state => ({
  formValues: getFormValues('my-very-own-form')(state),
});
const formConfiguration = {
  form: 'my-very-own-form',
}

export default connect(mapStateToProps)(
  reduxForm(formConfiguration)(FormContainer)
);

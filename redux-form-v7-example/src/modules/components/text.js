import React from 'react';

export const Text = props => {
  return (
    <div className="mv4 w-100">
      <div className="b sans-serif pv2 w-100">
        {props.label}
      </div>
      <input
        {...props.input}
        placeholder={props.label}
        type="text"
        className="pa2 ba b--black-40 w-100"
      />
      {props.meta && props.meta.error && props.meta.touched && (
        <div className="sans-serif red">
          {props.meta.error}
        </div>
      )}
    </div>
  );
}

export default Text;

import React from 'react';

export const Checkbox = props => {
  return (
    <div className="flex items-center mv4 w-100">
      <input
        {...props.input}
        className="mr2"
        type="checkbox"
        checked={props.input.value}
      />
      <div className="sans-serif">{props.label}</div>
    </div>
  );
}

export default Checkbox;

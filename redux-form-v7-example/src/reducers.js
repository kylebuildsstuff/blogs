import { combineReducers } from 'redux';
import { reducer as formReducer } from 'redux-form';

export default function createReducer(extraReducerObjects = {}) {
  return combineReducers({
    form: formReducer,
    ...extraReducerObjects
  });
}

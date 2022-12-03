import { configureStore } from '@reduxjs/toolkit';
import counterReducer from '../features/counter/counterSlice';
import companyReducer from '../features/company/companySlice';

export default configureStore({
  reducer: {
    counter: counterReducer,
    company: companyReducer,
  },
});

import { configureStore } from '@reduxjs/toolkit';
import loginReducer from '../features/login/loginSlice';
import pdfReducer from '../features/report/reportSlice';

export default configureStore({
  reducer: {
    login: loginReducer,
    pdf_info: pdfReducer,
  },
});

import styled, { keyframes } from 'styled-components';

export const keyFrameExampleOne = keyframes`
  0% {
    height: 200px;
  }
  30%, 100% {
    width: 400px;
  }
  100% {
    height: 600px;
    background: orange;
  }
`

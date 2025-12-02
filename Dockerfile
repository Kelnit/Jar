# Build Stage Stable Version
FROM golang:1.25.4-alpine AS builder

# Working Directory
WORKDIR /application

# Install Dependencies
RUN apk update && apk add --no-cache git

# Copy File to Application
COPY go.mod go.sum /application
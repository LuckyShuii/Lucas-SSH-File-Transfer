// __tests__/onValuesChange.spec.ts
import { describe, it, expect, beforeEach, vi } from 'vitest'
import type { SignUpPageProps } from '@/types/SignUpProps'
import { onValuesChange } from '@/components/SignUpPage/onValuesChange'

/**
 * @onValuesChange is a function that is called when the form values change
 * It checks if all required fields are filled and if the password and confirm password match to enable the submit button
 * @param {undefined} - first param: Not used here
 * @param {SignUpPageProps} allValues - second param: All values of the form
 * @param {Function} setIsDisabled - Function to set the disabled state of the submit button
 * @returns {void} - No return value
 */
describe('onValuesChange', () => {
    // Create a mock function for setIsDisabled
    // This function will be used to simulate the behavior of the setIsDisabled function
    const mockSetIsDisabled = vi.fn()

    /**
     * @baseValues is a helper function that returns a base set of values for the form
     * It is used to create a consistent set of values for the tests.
     * @returns {SignUpPageProps} - A base set of values for the form
     */
    const baseValues = (): SignUpPageProps => ({
        username: 'johndoe',
        email: 'john@doe.com',
        rgpd: true,
        password: 'Secr3t!',
        confirmPassword: 'Secr3t!',
    })

    /**
     * It checks if all required fields are filled and if the password and confirm password match to enable the submit button
     * @param {undefined} - Not used here
     * @param {SignUpPageProps} allValues - All values of the form
     * @param {Function} setIsDisabled - Function to set the disabled state of the submit button
     */
    beforeEach(() => {
        mockSetIsDisabled.mockClear()
    })
    
    /**
     * Test if the function is called with false when all required fields are filled and the password and confirm password match
     */
    it('triggers setIsDisabled(false) when all required fields are filled and password matches', () => {
        const allValues = baseValues()
        onValuesChange(undefined, allValues, mockSetIsDisabled)
        expect(mockSetIsDisabled).toHaveBeenCalledWith(false)
    })

    /**
     * Test if the function is called with true when a required field is missing
     */
    it('triggers setIsDisabled(true) when a required field is missing', () => {
        const allValues = { ...baseValues(), email: '' }
        onValuesChange(undefined, allValues, mockSetIsDisabled)
        expect(mockSetIsDisabled).toHaveBeenCalledWith(true)
    })

    /**
     * Test if the function is called with true when rgpd is false
     */
    it('triggers setIsDisabled(true) when rgpd is false', () => {
        const allValues = { ...baseValues(), rgpd: false }
        onValuesChange(undefined, allValues, mockSetIsDisabled)
        expect(mockSetIsDisabled).toHaveBeenCalledWith(true)
    })

    /**
     * Test if the function is called with true when password and confirmPassword do not match
     */
    it('triggers setIsDisabled(true) when password and confirmPassword do not match', () => {
        const allValues = { ...baseValues(), confirmPassword: 'autre' }
        onValuesChange(undefined, allValues, mockSetIsDisabled)
        expect(mockSetIsDisabled).toHaveBeenCalledWith(true)
    })

    /**
     * Test if the function is called with true when password is empty
     */
    it('triggers setIsDisabled(true) when password is empty', () => {
        const v1 = { ...baseValues(), password: '' }
        onValuesChange(undefined, v1, mockSetIsDisabled)
        const v2 = { ...baseValues(), confirmPassword: '' }
        onValuesChange(undefined, v2, mockSetIsDisabled)
        expect(mockSetIsDisabled).toHaveBeenCalledTimes(2)
        expect(mockSetIsDisabled).toHaveBeenNthCalledWith(1, true)
        expect(mockSetIsDisabled).toHaveBeenNthCalledWith(2, true)
    })
})
